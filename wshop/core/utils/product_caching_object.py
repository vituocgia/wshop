# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.models import Product
from wshop.core.utils.model_caching_descriptor import ModelCachingDescriptor


class ProductCachingObject(object):
    _descriptor = ModelCachingDescriptor("product", queryset=Product.objects.all())
    product = _descriptor.object_property
    product_id = _descriptor.id_property
