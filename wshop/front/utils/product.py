# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from collections import OrderedDict

import six
from django.utils.safestring import mark_safe
from django.utils.translation import get_language

from wshop.apps.provides import get_provide_objects
from wshop.core.models import (
    AttributeVisibility, ProductMode, ProductVariationResult, ShopProduct
)
from wshop.core.utils import context_cache
from wshop.front.utils.views import cache_product_things
from wshop.utils.numbers import get_string_sort_order


def get_product_context(request, product, language=None):   # noqa (C901)
    """
    Get product context

    Used in `wshop.front.views.product:ProductDetailView`

    :return: A context dict containing everything needed to render product view
    :rtype: dict
    """
    if not language:
        language = get_language()

    shop_product = product.get_shop_instance(request.shop)
    context = {}
    context["product"] = product
    context["category"] = shop_product.primary_category
    context["orderability_errors"] = list(shop_product.get_orderability_errors(
        supplier=None, quantity=1, customer=request.customer, ignore_minimum=True))
    context["variation_children"] = []
    if product.mode == ProductMode.SIMPLE_VARIATION_PARENT:
        context["variation_children"] = cache_product_things(
            request,
            sorted(
                product.variation_children.language(language).all(),
                key=lambda p: get_string_sort_order(p.variation_name or p.name)
            )
        )
        context["orderable_variation_children"] = []
        for p in context["variation_children"]:
            try:
                if p.get_shop_instance(request.shop).is_orderable(supplier=None, customer=request.customer, quantity=1):
                    context["orderable_variation_children"].append(p)
            except ShopProduct.DoesNotExist:
                pass

    elif product.mode == ProductMode.VARIABLE_VARIATION_PARENT:
        variation_variables = product.variation_variables.all().prefetch_related("values")
        orderable_children, is_orderable = get_orderable_variation_children(product, request, variation_variables)
        context["orderable_variation_children"] = orderable_children
        context["variation_orderable"] = is_orderable
        context["variation_variables"] = variation_variables
    elif product.is_container():
        children = product.get_all_package_children().translated().order_by("translations__name")
        context["package_children"] = cache_product_things(request, children)

    context["shop_product"] = shop_product
    context["attributes"] = product.attributes.filter(
        attribute__visibility_mode=AttributeVisibility.SHOW_ON_PRODUCT_PAGE)
    context["primary_image"] = shop_product.public_primary_image
    context["images"] = shop_product.public_images
    context["order_form"] = _get_order_form(request, context, product, language)

    for provide_object in get_provide_objects("product_context_extra"):
        provider = provide_object(request, product, language)
        if provider.provides_extra_context():
            context.update(provider.extra_context)

    return context


def _get_order_form(request, context, product, language):
    for obj in get_provide_objects("front_product_order_form"):
        product_order_form = obj(request, context, product, language)
        if product_order_form.is_compatible():
            return mark_safe(product_order_form.render())
    return None


def get_orderable_variation_children(product, request, variation_variables):    # noqa (C901)
    if not variation_variables:
        variation_variables = product.variation_variables.all().prefetch_related("values")

    key, val = context_cache.get_cached_value(
        identifier="orderable_variation_children", item=product, context=request,
        variation_variables=variation_variables)
    if val is not None:
        return val

    orderable_variation_children = OrderedDict()
    orderable = 0
    for combo_data in product.get_all_available_combinations():
        combo = combo_data["variable_to_value"]
        for k, v in six.iteritems(combo):
            if k not in orderable_variation_children:
                orderable_variation_children[k] = []

        res = ProductVariationResult.resolve(product, combo)
        try:
            shop_product = res.get_shop_instance(request.shop)
        except ShopProduct.DoesNotExist:
            continue

        if res and shop_product.is_orderable(
                supplier=None,
                customer=request.customer,
                quantity=1
        ):
            orderable += 1

            for k, v in six.iteritems(combo):
                if v not in orderable_variation_children[k]:
                    orderable_variation_children[k].append(v)

    values = (orderable_variation_children, orderable != 0)
    context_cache.set_cached_value(key, values)
    return values


class ProductContextExtra(object):

    def __init__(self, request, product, language, **kwargs):
        self.request = request
        self.product = product
        self.language = language

    def provides_extra_context(self):
        """
        Override to add business logic if this module has any context to be added
        to the product context data.
        """
        return (self.extra_context is not None)

    @property
    def extra_context(self):
        """
        Override this property to return wanted information to be added to the product context data.
        This property should return a dictionary which will be updated to the product context data.
        """
        return {}
