# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

import pytest
from bs4 import BeautifulSoup
from django.core.urlresolvers import reverse

from wshop.admin.views.wizard import WizardView
from wshop.apps.provides import override_provides
from wshop.core.models import (
    CustomCarrier, CustomPaymentProcessor, PaymentMethod, ServiceProvider,
    ShippingMethod, Shop, TaxClass
)
from wshop.testing.factories import (
    get_currency, get_default_shop, get_default_tax_class
)
from wshop.testing.soup_utils import extract_form_fields
from wshop.testing.utils import apply_request_middleware
from wshop.xtheme._theme import get_current_theme
from wshop.xtheme.testing import override_current_theme_class
from wshop_tests.xtheme.utils import FauxTheme


def _extract_fields(rf, user):
    request = apply_request_middleware(rf.get("/"), user=user)
    response = WizardView.as_view()(request)
    response.render()
    soup = BeautifulSoup(response.content)
    return extract_form_fields(soup.find("form"))


def assert_redirect_to_dashboard(rf, user, shop):
    request = apply_request_middleware(rf.get("/"), user=user, shop=shop)
    response = WizardView.as_view()(request)
    assert response.status_code == 302
    assert response["Location"] == reverse("wshop_admin:dashboard")


@pytest.mark.django_db
def test_get_wizard_no_panes(rf, settings, admin_user):
    shop = get_default_shop()
    settings.WSHOP_SETUP_WIZARD_PANE_SPEC = []
    assert_redirect_to_dashboard(rf, admin_user, shop)


@pytest.mark.django_db
def test_shop_wizard_pane(rf, admin_user, settings):
    settings.WSHOP_SETUP_WIZARD_PANE_SPEC = [
        "wshop.admin.modules.shops.views:ShopWizardPane"
    ]
    shop = Shop.objects.create()
    get_currency("USD")
    assert not shop.contact_address
    assert not TaxClass.objects.exists()
    fields = _extract_fields(rf, admin_user)
    fields["shop-logo"] = ""  # Correct init value for this is not None, but empty string
    request = apply_request_middleware(rf.post("/", data=fields), user=admin_user, shop=shop)
    response = WizardView.as_view()(request)
    # fields are missing
    assert response.status_code == 400
    fields["shop-public_name__fi"] = "test shop"
    fields["shop-currency"] = "USD"
    fields["address-name"] = "TEST"
    fields["address-city"] = "TEST"
    fields["address-region_code"] = "CA"
    fields["address-street"] = "test"
    fields["address-country"] = "US"

    request = apply_request_middleware(rf.post("/", data=fields), user=admin_user, shop=shop)
    response = WizardView.as_view()(request)
    assert response.status_code == 200
    shop.refresh_from_db()
    shop.set_current_language("fi")
    assert shop.name == "test shop"
    assert shop.public_name == "test shop"
    assert shop.logo is None
    assert shop.contact_address
    assert shop.currency == "USD"
    assert TaxClass.objects.exists()
    assert_redirect_to_dashboard(rf, admin_user, shop)


@pytest.mark.django_db
def test_shipping_method_wizard_pane(rf, admin_user, settings):
    settings.WSHOP_SETUP_WIZARD_PANE_SPEC = [
        "wshop.admin.modules.service_providers.views.CarrierWizardPane"
    ]
    shop = get_default_shop()
    get_default_tax_class()
    fields = _extract_fields(rf, admin_user)
    fields["shipping_method_base-providers"] = "manual_shipping"
    fields["manual_shipping-service_name"] = "test"

    request = apply_request_middleware(rf.post("/", data=fields), user=admin_user, shop=shop)
    response = WizardView.as_view()(request)
    assert response.status_code == 200
    assert ServiceProvider.objects.count() == 1
    assert CustomCarrier.objects.count() == 1
    assert CustomCarrier.objects.first().name == "Manual"
    assert ShippingMethod.objects.count() == 1
    assert ShippingMethod.objects.first().name == "test"
    assert_redirect_to_dashboard(rf, admin_user, shop)


@pytest.mark.django_db
def test_payment_method_wizard_pane(rf, admin_user, settings):
    settings.WSHOP_SETUP_WIZARD_PANE_SPEC = [
        "wshop.admin.modules.service_providers.views.PaymentWizardPane"
    ]
    shop = get_default_shop()
    get_default_tax_class()
    fields = _extract_fields(rf, admin_user)
    fields["payment_method_base-providers"] = "manual_payment"
    fields["manual_payment-service_name"] = "test"

    request = apply_request_middleware(rf.post("/", data=fields), user=admin_user)
    response = WizardView.as_view()(request)
    assert response.status_code == 200
    assert ServiceProvider.objects.count() == 1
    assert CustomPaymentProcessor.objects.count() == 1
    assert CustomPaymentProcessor.objects.first().name == "Manual"
    assert PaymentMethod.objects.count() == 1
    assert PaymentMethod.objects.first().name == "test"
    assert_redirect_to_dashboard(rf, admin_user, shop)


@pytest.mark.django_db
def test_xtheme_wizard_pane(rf, admin_user, settings):
    settings.WSHOP_SETUP_WIZARD_PANE_SPEC = [
        "wshop.xtheme.admin_module.views.ThemeWizardPane"
    ]
    shop = get_default_shop()
    with override_current_theme_class():
        with override_provides("xtheme", [
            "wshop_tests.xtheme.utils:FauxTheme"
        ]):
            assert get_current_theme(shop)
            fields = _extract_fields(rf, admin_user)
            fields["theme-activate"] = FauxTheme.identifier
            request = apply_request_middleware(rf.post("/", data=fields), user=admin_user)
            response = WizardView.as_view()(request)
            assert isinstance(get_current_theme(shop), FauxTheme)
            assert_redirect_to_dashboard(rf, admin_user, shop)