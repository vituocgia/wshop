# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from wshop.core.models import StockBehavior
from wshop.testing.factories import (
    create_random_person, get_default_shop, get_default_shop_product,
    get_default_supplier
)


@pytest.mark.django_db
def test_default_supplier():
    supplier = get_default_supplier()
    shop_product = get_default_shop_product()
    product = shop_product.product
    assert supplier.get_stock_statuses([product.id])[product.id].logical_count == 0
    assert not list(supplier.get_orderability_errors(shop_product, 1, customer=None))


@pytest.mark.django_db
def test_get_suppliable_products():
    customer = create_random_person()
    shop_product = get_default_shop_product()
    shop = get_default_shop()
    supplier = get_default_supplier()
    # Check for default orderable shop product with unstocked behavior
    assert len(list(supplier.get_suppliable_products(shop, customer=customer))) == 1

    product = shop_product.product
    product.stock_behavior = StockBehavior.STOCKED
    product.save()
    # Make sure supplier now omits unorderable product
    assert not list(supplier.get_suppliable_products(shop, customer=customer))
    assert len(list(supplier.get_orderability_errors(shop_product, quantity=1, customer=customer))) == 1

    shop_product.backorder_maximum = 10
    shop_product.save()

    assert len(list(supplier.get_suppliable_products(shop, customer=customer))) == 1
    assert len(list(supplier.get_orderability_errors(shop_product, quantity=10, customer=customer))) == 0
    assert len(list(supplier.get_orderability_errors(shop_product, quantity=11, customer=customer))) == 1

    shop_product.backorder_maximum = None
    shop_product.save()

    assert len(list(supplier.get_suppliable_products(shop, customer=customer))) == 1
    assert len(list(supplier.get_orderability_errors(shop_product, quantity=1000, customer=customer))) == 0
