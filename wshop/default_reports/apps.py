# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import wshop.apps


class AppConfig(wshop.apps.AppConfig):
    name = "wshop.default_reports"
    provides = {
        "reports": [
            "wshop.default_reports.reports.sales:SalesReport",
            "wshop.default_reports.reports.total_sales:TotalSales",
            "wshop.default_reports.reports.sales_per_hour:SalesPerHour",
            "wshop.default_reports.reports.product_total_sales:ProductSalesReport",
            "wshop.default_reports.reports.new_customers:NewCustomersReport",
            "wshop.default_reports.reports.customer_sales:CustomerSalesReport",
            "wshop.default_reports.reports.taxes:TaxesReport",
            "wshop.default_reports.reports.shipping:ShippingReport",
            "wshop.default_reports.reports.refunds.RefundedSalesReport",
        ],
    }
