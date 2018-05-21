# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

import wshop.apps


# TODO: Document how to create custom pricing modules (Refs WSHOP-514)
class CustomerGroupPricingAppConfig(wshop.apps.AppConfig):
    name = __name__
    verbose_name = _("Wshop Customer Group Pricing")
    label = "wshop_customer_group_pricing"
    provides = {
        "pricing_module": [
            __name__ + ".module:CustomerGroupPricingModule"
        ],
        "discount_module": [
            __name__ + ".module:CustomerGroupDiscountModule"
        ],
        "admin_product_form_part": [
            __name__ + ".admin_form_part:CustomerGroupPricingFormPart",
            __name__ + ".admin_form_part:CustomerGroupPricingDiscountFormPart"
        ],
        "api_populator": [
            __name__ + ".api:populate_customer_group_pricing_api"
        ]
    }


default_app_config = __name__ + ".CustomerGroupPricingAppConfig"
