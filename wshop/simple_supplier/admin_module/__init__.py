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
from wshop.admin.utils.urls import admin_url
from wshop.simple_supplier.models import StockAdjustment


class StocksAdminModule(AdminModule):
    name = _("Stock management")

    def get_urls(self):
        return [
            admin_url(
                "^adjust-stock/(?P<supplier_id>\d+)/(?P<product_id>\d+)/",
                "wshop.simple_supplier.admin_module.views.process_stock_adjustment",
                name="simple_supplier.stocks",
                permissions=get_default_model_permissions(StockAdjustment)
            ),
            admin_url(
                "^alert-limit/(?P<supplier_id>\d+)/(?P<product_id>\d+)/",
                "wshop.simple_supplier.admin_module.views.process_alert_limit",
                name="simple_supplier.alert_limits",
                permissions=get_default_model_permissions(StockAdjustment)
            ),
            admin_url(
                "^stocks/",
                "wshop.simple_supplier.admin_module.views.StocksListView",
                name="simple_supplier.stocks"
            ),
            admin_url(
                "^list-settings/",
                "wshop.admin.modules.settings.views.ListSettingsView",
                name="simple_supplier.list_settings",
                permissions=get_default_model_permissions(StockAdjustment),
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(StockAdjustment)

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-cubes",
                url="wshop_admin:simple_supplier.stocks",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="settings",
                ordering=6
            )
        ]
