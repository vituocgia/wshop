# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.api.address import MutableAddressViewSet
from wshop.core.api.attribute import AttributeViewSet
from wshop.core.api.basket import BasketViewSet
from wshop.core.api.category import CategoryViewSet
from wshop.core.api.contacts import ContactViewSet, PersonContactViewSet
from wshop.core.api.front_orders import FrontOrderViewSet
from wshop.core.api.front_passwords import (
    PasswordResetViewSet, SetPasswordViewSet
)
from wshop.core.api.front_products import (
    FrontProductViewSet, FrontShopProductViewSet
)
from wshop.core.api.front_users import FrontUserViewSet
from wshop.core.api.manufacturer import ManufacturerViewSet
from wshop.core.api.orders import OrderViewSet
from wshop.core.api.product_media import ProductMediaViewSet
from wshop.core.api.product_variation import (
    ProductVariationVariableValueViewSet, ProductVariationVariableViewSet
)
from wshop.core.api.products import (
    ProductAttributeViewSet, ProductPackageViewSet, ProductTypeViewSet,
    ProductViewSet, ShopProductViewSet
)
from wshop.core.api.shipments import ShipmentViewSet
from wshop.core.api.shop import ShopViewSet
from wshop.core.api.suppliers import SupplierViewSet
from wshop.core.api.tax import TaxViewSet
from wshop.core.api.tax_class import TaxClassViewSet
from wshop.core.api.units import SalesUnitViewSet
from wshop.core.api.users import UserViewSet


def populate_core_api(router):
    """
    :param router: Router
    :type router: rest_framework.routers.DefaultRouter
    """
    router.register("wshop/address", MutableAddressViewSet)
    router.register("wshop/attribute", AttributeViewSet)
    router.register("wshop/category", CategoryViewSet)
    router.register("wshop/contact", ContactViewSet)
    router.register("wshop/order", OrderViewSet)
    router.register("wshop/person_contact", PersonContactViewSet)
    router.register("wshop/product", ProductViewSet)
    router.register("wshop/product_attribute", ProductAttributeViewSet)
    router.register("wshop/product_media", ProductMediaViewSet)
    router.register("wshop/product_type", ProductTypeViewSet)
    router.register("wshop/product_package", ProductPackageViewSet)
    router.register("wshop/product_variation_variable", ProductVariationVariableViewSet)
    router.register("wshop/product_variation_variable_value", ProductVariationVariableValueViewSet)
    router.register("wshop/shipment", ShipmentViewSet)
    router.register("wshop/shop", ShopViewSet)
    router.register("wshop/shop_product", ShopProductViewSet)
    router.register("wshop/manufacturer", ManufacturerViewSet)
    router.register("wshop/supplier", SupplierViewSet)
    router.register("wshop/user", UserViewSet)
    router.register("wshop/sales_unit", SalesUnitViewSet)
    router.register("wshop/tax", TaxViewSet)
    router.register("wshop/tax_class", TaxClassViewSet)
    router.register("wshop/basket", BasketViewSet)

    router.register("wshop/front/user", FrontUserViewSet)
    router.register("wshop/front/password", SetPasswordViewSet, 'set_password')
    router.register("wshop/front/password/reset", PasswordResetViewSet, 'password_reset')
    router.register("wshop/front/orders", FrontOrderViewSet)
    router.register("wshop/front/shop_products", FrontShopProductViewSet)
    router.register("wshop/front/products", FrontProductViewSet)
