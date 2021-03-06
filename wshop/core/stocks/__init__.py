# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.utils.product_caching_object import ProductCachingObject


class ProductStockStatus(ProductCachingObject):
    def __init__(self, product=None, product_id=None, logical_count=0, physical_count=0, message=None, error=None):
        if product_id:
            self.product_id = product_id
        else:
            self.product = product
        if not self.product_id:
            raise ValueError("`ProductStockStatus` object must be bound to Products")
        self.logical_count = logical_count
        self.physical_count = physical_count
        self.message = message
        self.error = error
