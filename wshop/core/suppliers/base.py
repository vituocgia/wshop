# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.exceptions import ValidationError
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from wshop.core.models import StockBehavior
from wshop.core.stocks import ProductStockStatus
from wshop.utils.excs import Problem

from .enums import StockAdjustmentType


class BaseSupplierModule(object):
    """
    Base supplier module implementation.
    """

    identifier = None
    name = None

    def __init__(self, supplier, options):
        """
        :type supplier: Supplier
        :type options: dict
        """
        self.supplier = supplier
        self.options = options

    def get_stock_statuses(self, product_ids):
        """
        :param product_ids: Iterable of product IDs
        :return: Dict of {product_id: ProductStockStatus}
        :rtype: dict[int, wshop.core.stocks.ProductStockStatus]
        """
        return dict((
            product_id,
            ProductStockStatus(product_id=product_id, logical_count=0, physical_count=0)
        ) for product_id in product_ids)

    def get_stock_status(self, product_id):
        """
        :param product_id: Product ID
        :type product_id: int
        :rtype: wshop.core.stocks.ProductStockStatus
        """
        return self.get_stock_statuses([product_id])[product_id]

    def get_orderability_errors(self, shop_product, quantity, customer):
        """
        :param shop_product: Shop Product
        :type shop_product: wshop.core.models.ShopProduct
        :param quantity: Quantity to order
        :type quantity: decimal.Decimal
        :param customer: Contact
        :type user: django.contrib.auth.models.AbstractUser
        :rtype: iterable[ValidationError]
        """
        stock_status = self.get_stock_status(shop_product.product_id)
        backorder_maximum = shop_product.backorder_maximum
        if stock_status.error:
            yield ValidationError(stock_status.error, code="stock_error")
        if shop_product.product.stock_behavior == StockBehavior.STOCKED:
            if backorder_maximum is not None and quantity > stock_status.logical_count + backorder_maximum:
                yield ValidationError(stock_status.message or _(u"Insufficient stock"), code="stock_insufficient")

    def adjust_stock(self, product_id, delta, created_by=None, type=StockAdjustmentType.INVENTORY):
        raise NotImplementedError("Not implemented in BaseSupplierModule")

    def update_stock(self, product_id):
        pass  # no-op in BaseSupplierModule

    def update_stocks(self, product_ids):
        # Naive default implementation; smarter modules can do something better
        for product_id in product_ids:
            self.update_stock(product_id)

    def ship_products(self, shipment, product_quantities):
        insufficient_stocks = {}
        for product, quantity in product_quantities.items():
            if quantity > 0:
                stock_status = self.get_stock_status(product.pk)
                if (product.stock_behavior == StockBehavior.STOCKED) and (stock_status.physical_count < quantity):
                    insufficient_stocks[product] = stock_status.physical_count
                sp = shipment.products.create(product=product, quantity=quantity)
                sp.cache_values()
                sp.save()

        if insufficient_stocks:
            formatted_counts = [_("%(name)s (physical stock: %(quantity)s)") % {
                "name": force_text(name),
                "quantity": force_text(quantity)
            }
                                for (name, quantity) in insufficient_stocks.items()]
            raise Problem(
                _("Insufficient physical stock count for following products: %(product_counts)s") % {
                    "product_counts": ", ".join(formatted_counts)
                })

        shipment.cache_values()
        shipment.save()
