# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from wshop.admin.shop_provider import get_shop


class WshopAdminMiddleware(object):
    """
    Handle Wshop Admin specific tasks for each request and response.

    * Sets the current shop from the request
      ``request.shop`` : :class:`wshop.core.models.Shop`
          Currently active Shop.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        # we only care about Wshop Admin requests
        if request.resolver_match.app_name == "wshop_admin":
            shop = get_shop(request)
            if shop:
                request.shop = shop
