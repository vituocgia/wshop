# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from wshop.admin.modules.services import PaymentMethodModule, ShippingMethodModule

from wshop.admin.modules.manufacturers import ManufacturerModule

from wshop.admin.modules.product_types import ProductTypeModule

from wshop.admin.module_registry import replace_modules
from wshop.admin.modules.categories import CategoryModule
from wshop.admin.modules.products import ProductModule
from wshop.admin.modules.products.views import ProductEditView
from wshop.importer.admin_module import ImportAdminModule
from wshop.testing.factories import create_product
from wshop.testing.factories import get_default_shop
from wshop.testing.utils import apply_request_middleware
from wshop_tests.admin.utils import admin_only_urls


@pytest.mark.django_db
def test_campaigned_product_view(rf, admin_user):
    shop = get_default_shop()
    product = create_product("test-product", shop, default_price=200)
    shop_product = product.get_shop_instance(shop)

    request = apply_request_middleware(rf.get("/"), user=admin_user)

    with replace_modules([CategoryModule, ImportAdminModule, ProductModule,
                          ProductTypeModule, ManufacturerModule, PaymentMethodModule, ShippingMethodModule]):
        with admin_only_urls():
            render_product_view(shop_product, request)
            product2 = create_product("test-product2", shop)
            sp2 = product2.get_shop_instance(shop)
            render_product_view(sp2, request)  # should not break even though shop_product is not available


def render_product_view(shop_product, request):
    view_func = ProductEditView.as_view()
    response = view_func(request, pk=shop_product.pk)
    assert (shop_product.product.sku in response.rendered_content)  # it's probable the SKU is there
    response = view_func(request, pk=None)  # "new mode"
    assert response.rendered_content  # yeah, something gets rendered
