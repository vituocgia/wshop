# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.core.urlresolvers import reverse

from wshop.apps.provides import override_provides
from wshop.front.utils.product import ProductContextExtra
from wshop.front.views.product import ProductDetailView
from wshop.core.models import ProductMode
from wshop.testing.factories import (
    create_product, get_default_product, get_default_shop
)
from wshop.testing.utils import apply_request_middleware


@pytest.mark.django_db
def test_product_page(client):
    get_default_shop()
    product = get_default_product()
    response = client.get(
        reverse('wshop:product', kwargs={
            'pk': product.pk,
            'slug': product.slug
            }
        )
    )
    assert b'no such element' not in response.content, 'All items are not rendered correctly'
    # TODO test purchase_multiple and  sales_unit.allow_fractions

    product_mode_forms = [
        "wshop.front.forms.order_forms:VariableVariationProductOrderForm",
        "wshop.front.forms.order_forms:SimpleVariationProductOrderForm",
        "wshop.front.forms.order_forms:SimpleProductOrderForm",
        "wshop.testing.extend_classes:DifferentProductOrderForm"
    ]

    with override_provides("front_product_order_form", product_mode_forms):
        get_default_shop()
        product = get_default_product()
        product_modes = [ProductMode.NORMAL, ProductMode.PACKAGE_PARENT,
                         ProductMode.VARIABLE_VARIATION_PARENT, ProductMode.SIMPLE_VARIATION_PARENT,
                         ProductMode.SUBSCRIPTION]

        for product_mode in product_modes:
            product.mode = product_mode
            product.save()

            response = client.get(
                reverse('wshop:product', kwargs={
                    'pk': product.pk,
                    'slug': product.slug
                }
                        )
            )
            assert b'no such element' not in response.content, 'All items are not rendered correctly'
            if product_mode == ProductMode.SUBSCRIPTION:
                assert b'This is different' in response.content, 'DifferentProductOrderForm not rendered properly'
            # TODO test purchase_multiple and  sales_unit.allow_fractions



@pytest.mark.django_db
def test_package_product_page(client):
    shop = get_default_shop()
    parent = create_product("test-sku-1", shop=shop)
    child = create_product("test-sku-2", shop=shop)
    parent.make_package({child: 2})
    assert parent.is_package_parent()

    response = client.get(
        reverse('wshop:product', kwargs={
            'pk': parent.pk,
            'slug': parent.slug
            }
        )
    )
    assert b'no such element' not in response.content, 'All items are not rendered correctly'


class ExtraContextTest(ProductContextExtra):

    @property
    def extra_context(self):
        return {"product_sku": self.product.sku}


@pytest.mark.django_db
def test_product_view_extra_context(rf, admin_user):
    product = get_default_product()
    request = apply_request_middleware(rf.get("/"), user=admin_user)
    view_func = ProductDetailView.as_view()

    # Test that we can insert extra information into ProductDetailView context
    with override_provides("product_context_extra", [
        "wshop_tests.front.test_product:ExtraContextTest",
    ]):
        response = view_func(request, pk=product.pk)
        assert response.context_data['product_sku'] == product.sku
