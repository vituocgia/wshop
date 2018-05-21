# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class WshopSimpleSupplierAppConfig(AppConfig):
    name = "wshop.simple_supplier"
    verbose_name = "Wshop Simple Supplier"
    label = "simple_supplier"
    provides = {
        "supplier_module": [
            "wshop.simple_supplier.module:SimpleSupplierModule"
        ],
        "admin_product_form_part": [
            "wshop.simple_supplier.admin_module.forms:SimpleSupplierFormPart"
        ],
        "admin_module": [
            "wshop.simple_supplier.admin_module:StocksAdminModule"
        ],
        "notify_event": [
            "wshop.simple_supplier.notify_events:AlertLimitReached"
        ],
        "notify_script_template": [
            "wshop.simple_supplier.notify_script_template:StockLimitEmailScriptTemplate",
        ]
    }


default_app_config = "wshop.simple_supplier.WshopSimpleSupplierAppConfig"
