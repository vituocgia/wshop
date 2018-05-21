# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.core.pricing import TaxfulPrice, TaxlessPrice


class TaxedPrice(object):
    """
    Price with calculated taxes.

    .. attribute:: taxful

       (`~wshop.core.pricing.TaxfulPrice`)
       Price including taxes.

    .. attribute:: taxless

       (`~wshop.core.pricing.TaxlessPrice`)
       Pretax price.

    .. attribute:: taxes

       (`list[wshop.core.taxing.LineTax]`)
       List of taxes applied to the price.
    """
    def __init__(self, taxful, taxless, taxes=None):
        """
        Initialize from given prices and taxes.

        :type taxful: wshop.core.pricing.TaxfulPrice
        :param taxful: Price including taxes.
        :type taxless: wshop.core.pricing.TaxlessPrice
        :param taxless: Pretax price.
        :type taxes: list[wshop.core.taxing.LineTax]|None
        :param taxes: List of taxes applied to the price.
        """
        assert isinstance(taxful, TaxfulPrice)
        assert isinstance(taxless, TaxlessPrice)

        self.taxful = taxful
        self.taxless = taxless
        self.taxes = taxes or []

        # Validation
        expected_taxful_amount = taxless.amount + self.tax_amount
        assert abs(taxful.amount - expected_taxful_amount).value < 0.00001

    @property
    def tax_amount(self):
        """
        Total amount of applied taxes.
        """
        zero = self.taxful.new(0).amount
        return sum((x.amount for x in self.taxes), zero)

    @property
    def tax_rate(self):
        """
        Tax rate calculated from taxful and taxless amounts.
        """
        return (self.taxful.amount / self.taxless.amount) - 1
