# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.models import Supplier
from wshop.testing.factories import get_default_shop

IDENTIFIER = "test_simple_supplier"


def get_simple_supplier():
    supplier = Supplier.objects.filter(identifier=IDENTIFIER).first()
    if not supplier:
        supplier = Supplier.objects.create(
            identifier=IDENTIFIER,
            name="Simple Supplier",
            module_identifier="simple_supplier",
        )
    shop = get_default_shop()
    supplier.shops.add(shop)
    return supplier
