# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule
from wshop.admin.currencybound import CurrencyBound


class SalesDashboardModule(CurrencyBound, AdminModule):
    name = _("Sales Dashboard")

    def get_required_permissions(self):
        return ("wshop.view_sales_dashboard",)

    def get_dashboard_blocks(self, request):
        import wshop.admin.modules.sales_dashboard.dashboard as dashboard
        currency = self.currency
        if not currency:
            shop = request.shop
            currency = shop.currency

        yield dashboard.get_sales_of_the_day_block(request, currency)
        yield dashboard.get_lifetime_sales_block(request, currency)
        yield dashboard.get_avg_purchase_size_block(request, currency)
        yield dashboard.get_open_orders_block(request, currency)
        yield dashboard.get_order_value_chart_dashboard_block(request, currency)
        yield dashboard.get_shop_overview_block(request, currency)
        yield dashboard.get_recent_orders_block(request, currency)
