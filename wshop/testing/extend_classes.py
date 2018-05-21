# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.models import ProductMode
from wshop.front.forms.order_forms import ProductOrderForm


class DifferentProductOrderForm(ProductOrderForm):
    template_name = "wshop_testing/different_order_form.jinja"

    def is_compatible(self):
        return (self.product.mode == ProductMode.SUBSCRIPTION)
