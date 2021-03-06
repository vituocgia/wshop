# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.utils import timezone

import wshop.core.models
from wshop.admin.urls import login
from wshop.core.models import (
    AnonymousContact, CompanyContact, Contact, get_company_contact,
    get_person_contact, PersonContact, Shop
)
from wshop.front.middleware import WshopFrontMiddleware
from wshop.front.views.index import IndexView
from wshop.testing.factories import create_random_company, get_default_shop
from wshop.testing.utils import apply_request_middleware
from wshop_tests.utils.fixtures import regular_user

from .fixtures import get_request

__all__ = ("regular_user",)  # noqa


def get_unprocessed_request():
    request = get_request()
    for attrname in ['shop', 'person', 'customer', 'basket']:
        assert not hasattr(request, attrname)
    return request


def check_request_attribute_basics(request):
    assert isinstance(request.shop, Shop)
    assert isinstance(request.person, Contact)
    assert isinstance(request.customer, Contact)
    assert isinstance(request.basket, wshop.front.basket.objects.BaseBasket)


# TODO: Make these tests faster by faking the Shop and not using database


@pytest.mark.django_db
def test_with_anonymous_user():
    get_default_shop()  # Create a shop

    mw = WshopFrontMiddleware()
    request = get_unprocessed_request()

    mw.process_request(request)

    check_request_attribute_basics(request)

    assert isinstance(request.person, AnonymousContact)
    assert isinstance(request.customer, AnonymousContact)
    assert request.person == request.customer


@pytest.mark.django_db
def test_with_logged_in_user(regular_user):
    get_default_shop()  # Create a shop

    mw = WshopFrontMiddleware()
    request = get_unprocessed_request()
    request.user = regular_user

    mw.process_request(request)

    check_request_attribute_basics(request)

    assert isinstance(request.person, PersonContact)
    assert isinstance(request.customer, PersonContact)
    assert request.person == request.customer


@pytest.mark.django_db
def test_customer_company_member(regular_user):
    get_default_shop()  # Create a shop

    mw = WshopFrontMiddleware()
    request = get_unprocessed_request()
    request.user = regular_user
    person = get_person_contact(regular_user)
    company = create_random_company()
    company.members.add(person)

    assert get_company_contact(regular_user) == company

    mw.process_request(request)

    check_request_attribute_basics(request)

    assert isinstance(request.person, PersonContact)
    assert isinstance(request.customer, CompanyContact)

    company = get_company_contact(request.user)
    assert company and (company == request.customer)


@pytest.mark.django_db
def test_timezone_setting(regular_user):
    get_default_shop()  # Create a shop

    mw = WshopFrontMiddleware()
    request = get_unprocessed_request()
    request.user = regular_user

    some_tz = ('US/Hawaii' if settings.TIME_ZONE == 'UTC' else 'UTC')

    person = get_person_contact(regular_user)
    person.timezone = some_tz
    person.save()

    assert timezone.get_current_timezone_name() != some_tz

    mw.process_request(request)

    assert timezone.get_current_timezone_name() == some_tz


@pytest.mark.django_db
def test_intra_request_user_changing(rf, regular_user):
    get_default_shop()  # Create a shop
    mw = WshopFrontMiddleware()
    request = apply_request_middleware(rf.get("/"), user=regular_user)
    mw.process_request(request)
    assert request.person == get_person_contact(regular_user)
    logout(request)
    assert request.user == AnonymousUser()
    assert request.person == AnonymousContact()
    assert request.customer == AnonymousContact()


@pytest.mark.django_db
def test_maintenance_mode(rf, regular_user, admin_user):
    shop = get_default_shop()
    shop.maintenance_mode = True
    shop.save()

    mw = WshopFrontMiddleware()

    request = apply_request_middleware(rf.get("/"), user=regular_user)
    maintenance_response = mw.process_view(request, IndexView)
    assert maintenance_response is not None
    assert maintenance_response.status_code == 503
    assert mw._get_maintenance_response(request, IndexView).content == maintenance_response.content

    login_response = mw.process_view(request, login)
    assert login_response is None

    request = apply_request_middleware(rf.get("/"), user=admin_user)
    admin_response = mw.process_view(request, IndexView)
    assert admin_response is None

    shop.maintenance_mode = False
    shop.save()


@pytest.mark.django_db
def test_with_inactive_contact(rf, regular_user, admin_user):
    get_default_shop()  # Create a shop
    # Get or create contact for regular user
    contact = get_person_contact(regular_user)
    assert contact.is_active
    contact.is_active = False
    contact.save()

    request = apply_request_middleware(rf.get("/"), user=regular_user)
    mw = WshopFrontMiddleware()
    mw.process_request(request)

    assert request.user == AnonymousUser()
    assert request.person == AnonymousContact()
    assert request.customer == AnonymousContact()
