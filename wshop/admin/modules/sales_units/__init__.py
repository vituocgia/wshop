# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import STOREFRONT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from wshop.core.models import DisplayUnit, SalesUnit


class SalesUnitModule(AdminModule):
    name = _("Sales Units")
    breadcrumbs_menu_entry = MenuEntry(name, url="wshop_admin:sales_unit.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^sales-units",
            view_template="wshop.admin.modules.sales_units.views.SalesUnit%sView",
            name_template="sales_unit.%s",
            permissions=get_default_model_permissions(SalesUnit)
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-asterisk",
                url="wshop_admin:sales_unit.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="settings",
                ordering=5
            ),
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(SalesUnit)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(SalesUnit, "wshop_admin:sales_unit", object, kind)


class DisplayUnitModule(AdminModule):
    name = _("Display Units")
    breadcrumbs_menu_entry = MenuEntry(name, url="wshop_admin:display_unit.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^display-units",
            view_template="wshop.admin.modules.sales_units.views.DisplayUnit%sView",
            name_template="display_unit.%s",
            permissions=get_default_model_permissions(DisplayUnit)
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-asterisk",
                url="wshop_admin:display_unit.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="settings",
                ordering=5
            ),
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(DisplayUnit)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(DisplayUnit, "wshop_admin:display_unit", object, kind)
