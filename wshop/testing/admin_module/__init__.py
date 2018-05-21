# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import SETTINGS_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url
from wshop.core.models import Shop


class TestingAdminModule(AdminModule):
    def get_urls(self):
        return [
            admin_url(
                "^mocker/$",
                "wshop.testing.admin_module.mocker_view.MockerView",
                name="mocker",
                permissions=get_default_model_permissions(Shop)
            )
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text="Create Mock Objects",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="data_transfer",
                url="wshop_admin:mocker",
                icon="fa fa-star"
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(Shop)
