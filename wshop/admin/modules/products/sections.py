# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext as _

from wshop.admin.base import Section
from wshop.core.models import Order


class ProductOrdersSection(Section):
    identifier = "product_orders"
    name = _("Orders")
    icon = "fa-inbox"
    template = "wshop/admin/products/_product_orders.jinja"
    order = 1

    @classmethod
    def visible_for_object(cls, product, request=None):
        has_product_id = bool(product.pk)
        if not request:
            return has_product_id
        return bool(request.user.has_perm('wshop.view_product') and has_product_id)

    @classmethod
    def get_context_data(cls, product, request=None):
        # TODO: restrict to first 100 orders - do pagination later
        return Order.objects.valid().filter(lines__product_id=product.id).distinct()[:100]
