# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig
from wshop.apps.settings import validate_templates_configuration


class WshopFrontAppConfig(AppConfig):
    name = "wshop.front"
    verbose_name = "Wshop Frontend"
    label = "wshop_front"

    provides = {
        "admin_category_form_part": [
            "wshop.front.admin_module.sorts_and_filters.form_parts.ConfigurationCategoryFormPart"
        ],
        "admin_module": [
            "wshop.front.admin_module.CartAdminModule",
        ],
        "admin_shop_form_part": [
            "wshop.front.admin_module.sorts_and_filters.form_parts.ConfigurationShopFormPart",
            "wshop.front.admin_module.checkout.form_parts.CheckoutShopFormPart"
        ],
        "notify_event": [
            "wshop.front.notify_events:OrderReceived",
            "wshop.front.notify_events:ShipmentCreated",
            "wshop.front.notify_events:ShipmentDeleted",
            "wshop.front.notify_events:PaymentCreated",
            "wshop.front.notify_events:RefundCreated",
        ],
        "notify_script_template": [
            "wshop.front.notify_script_templates:PaymentCreatedEmailScriptTemplate",
            "wshop.front.notify_script_templates:RefundCreatedEmailScriptTemplate",
            "wshop.front.notify_script_templates:ShipmentDeletedEmailScriptTemplate",
            "wshop.front.notify_script_templates:OrderConfirmationEmailScriptTemplate",
            "wshop.front.notify_script_templates:ShipmentCreatedEmailScriptTemplate",
        ],
        "front_extend_product_list_form": [
            "wshop.front.forms.product_list_modifiers.CategoryProductListFilter",
            "wshop.front.forms.product_list_modifiers.LimitProductListPageSize",
            "wshop.front.forms.product_list_modifiers.ProductPriceFilter",
            "wshop.front.forms.product_list_modifiers.ProductVariationFilter",
            "wshop.front.forms.product_list_modifiers.SortProductListByCreatedDate",
            "wshop.front.forms.product_list_modifiers.SortProductListByAscendingCreatedDate",
            "wshop.front.forms.product_list_modifiers.SortProductListByName",
            "wshop.front.forms.product_list_modifiers.SortProductListByPrice",
            "wshop.front.forms.product_list_modifiers.ManufacturerProductListFilter",
        ],
        "front_product_order_form": [
            "wshop.front.forms.order_forms:VariableVariationProductOrderForm",
            "wshop.front.forms.order_forms:SimpleVariationProductOrderForm",
            "wshop.front.forms.order_forms:SimpleProductOrderForm",
        ],
    }

    def ready(self):
        # connect signals
        import wshop.front.notify_events  # noqa: F401

        validate_templates_configuration()


default_app_config = "wshop.front.WshopFrontAppConfig"
