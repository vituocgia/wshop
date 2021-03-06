# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.views.generic import ListView

from wshop.core.models import Product
from wshop.front.template_helpers.product import is_visible
from wshop.front.utils.sorts_and_filters import (
    get_product_queryset, get_query_filters, post_filter_products,
    ProductListForm, sort_products
)
from wshop.front.utils.views import cache_product_things


class SearchView(ListView):
    form_class = ProductListForm
    template_name = "wshop/simple_search/search.jinja"
    model = Product
    context_object_name = "products"

    def dispatch(self, request, *args, **kwargs):
        self.form = ProductListForm(
            request=self.request, shop=self.request.shop, category=None, data=self.request.GET)
        return super(SearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if not self.form.is_valid():
            return Product.objects.none()
        data = self.form.cleaned_data
        if not (data and data.get("q")):  # pragma: no cover
            return Product.objects.none()
        products = Product.objects.filter(get_query_filters(self.request, None, data=data))
        return get_product_queryset(products, self.request, None, data)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context["form"] = self.form
        products = context["products"]
        if products:
            data = self.form.cleaned_data
            products = post_filter_products(self.request, None, products, data)
            products = cache_product_things(self.request, products)
            products = sort_products(self.request, None, products, data)
            products = [p for p in products if is_visible({"request": self.request}, p)]
            context["products"] = products
        context["no_results"] = (self.form.is_valid() and not products)
        return context
