# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.models import Shop
from wshop.core.utils.shops import get_shop_from_host
from wshop.utils.importing import cached_load


class DefaultShopProvider(object):
    @classmethod
    def get_shop(cls, request, **kwargs):
        shop = None

        host = request.META.get("HTTP_HOST")
        if host:
            shop = get_shop_from_host(host)

        if not shop:
            shop = Shop.objects.first()

        return shop


def get_shop(request, **kwargs):
    return cached_load("WSHOP_REQUEST_SHOP_PROVIDER_SPEC").get_shop(request, **kwargs)
