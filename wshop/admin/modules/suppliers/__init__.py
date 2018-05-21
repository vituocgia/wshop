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
from wshop.core.models import Supplier


class SupplierModule(AdminModule):
    name = _("Suppliers")
    breadcrumbs_menu_entry = MenuEntry(name, url="wshop_admin:supplier.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^suppliers",
            view_template="wshop.admin.modules.suppliers.views.Supplier%sView",
            name_template="supplier.%s",
            permissions=get_default_model_permissions(Supplier)
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Suppliers"),
                icon="fa fa-truck",
                url="wshop_admin:supplier.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="settings",
                ordering=7
            ),
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(Supplier)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Supplier, "wshop_admin:supplier", object, kind)
