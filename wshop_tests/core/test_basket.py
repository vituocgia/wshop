# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.test.utils import override_settings

from wshop.core.basket import get_basket
from wshop.core.models import get_person_contact, OrderLineType
from wshop.testing import factories
from wshop.testing.utils import apply_request_middleware

CORE_BASKET_SETTINGS = dict(
    WSHOP_BASKET_ORDER_CREATOR_SPEC="wshop.core.basket.order_creator:BasketOrderCreator",
    WSHOP_BASKET_STORAGE_CLASS_SPEC="wshop.core.basket.storage:DatabaseBasketStorage",
    WSHOP_BASKET_CLASS_SPEC="wshop.core.basket.objects:Basket"
)

@pytest.mark.django_db
def test_set_customer_with_custom_basket_lines(rf):
    """
    Set anonymous to the basket customer
    """
    with override_settings(**CORE_BASKET_SETTINGS):
        factories.get_default_shop()
        user = factories.create_random_user()
        request = apply_request_middleware(rf.get("/"), user=user)
        basket = get_basket(request, "basket")

        base_unit_price = basket.shop.create_price("10.99")

        basket.add_line(text="Custom Line",
                        type=OrderLineType.OTHER,
                        line_id="random-you-know",
                        shop=basket.shop,
                        quantity=1,
                        base_unit_price=base_unit_price)

        basket.customer = get_person_contact(user)
        basket.refresh_lines()
        basket.save()
        assert basket.customer == get_person_contact(user)
