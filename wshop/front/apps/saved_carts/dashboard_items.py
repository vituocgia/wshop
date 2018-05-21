# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from wshop.front.models import StoredBasket
from wshop.front.utils.dashboard import DashboardItem


class SavedCartsItem(DashboardItem):
    template_name = "wshop/saved_carts/dashboard_item.jinja"
    title = _("Saved Carts")
    icon = "fa fa-shopping-cart"
    _url = "wshop:saved_cart.list"

    def get_context(self):
        context = super(SavedCartsItem, self).get_context()
        context["carts"] = StoredBasket.objects.filter(
            persistent=True, deleted=False, customer=self.request.customer, shop=self.request.shop)
        return context
