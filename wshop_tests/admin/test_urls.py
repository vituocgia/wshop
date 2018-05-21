# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from collections import Counter

import pytest
from django.core.exceptions import ImproperlyConfigured

from wshop.admin.utils.urls import admin_url, get_model_url, NoModelUrl
from wshop.testing.factories import get_default_product, get_default_shop
from wshop_tests.admin.utils import admin_only_urls
from wshop_tests.utils.faux_users import StaffUser


@pytest.mark.django_db
def test_model_url():
    with admin_only_urls():
        with pytest.raises(NoModelUrl):
            get_model_url(Counter)  # That's silly!
        p = get_default_product()

        assert get_model_url(p, shop=get_default_shop())


@pytest.mark.django_db
def test_model_url_with_permissions():
    permissions = set(["wshop.add_product", "wshop.delete_product", "wshop.change_product"])
    shop = get_default_shop()

    p = get_default_product()

    # If no user is given, don't check for permissions
    assert get_model_url(p, shop=shop)

    # If a user is given and no permissions are provided, check for default model permissions
    user = StaffUser()
    with pytest.raises(NoModelUrl):
        assert get_model_url(p, user=user, shop=shop)

    # If a user is given and permissions are provided, check for those permissions
    assert get_model_url(p, user=user, required_permissions=(), shop=shop)
    with pytest.raises(NoModelUrl):
        assert get_model_url(p, user=user, required_permissions=["wshop.add_product"], shop=shop)

    # Confirm that url is returned with correct permissions
    user.permissions = permissions
    assert get_model_url(p, user=user, shop=shop)
    assert get_model_url(p, user=user, required_permissions=permissions, shop=shop)


def test_invalid_admin_url():
    with pytest.raises(ImproperlyConfigured):
        admin_url("", "")


def test_admin_url_prefix():
    assert admin_url("", "foo", prefix="bar")._callback_str == "bar.foo"
