# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import unicode_literals

import six

import wshop.core.models
import wshop.utils.money


class LineTax(object):
    """
    Tax of some line.

    This is an interface for specifying taxes of an `OrderLine` or
    `SourceLine`.

    .. attribute:: tax

       (`~wshop.core.models.Tax`)
       The tax that this line is about.

    .. attribute:: name

       (`str`)
       Name of the tax.

    .. attribute:: amount

       (`~wshop.utils.money.Money`)
       Tax amount.

    .. attribute:: base_amount

       (`~wshop.utils.money.Money`)
       Amount that this tax is calculated from.
    """

    @property
    def rate(self):
        if not self.base_amount:
            return self.tax.rate
        return (self.amount / self.base_amount)

    @classmethod
    def from_tax(cls, tax, base_amount, **kwargs):
        """
        Create tax line for given tax and base amount.

        :type cls: type
        :type tax: wshop.core.models.Tax
        :type base_amount: wshop.utils.money.Money
        """
        return cls(
            tax=tax,
            name=tax.name,
            base_amount=base_amount,
            amount=tax.calculate_amount(base_amount),
            **kwargs
        )


class SourceLineTax(LineTax):
    def __init__(self, tax, name, amount, base_amount):
        """
        Initialize line tax from given values.

        :type tax: wshop.core.models.Tax
        :type name: six.text_type
        :type amount: wshop.utils.money.Money
        :type base_amount: wshop.utils.money.Money
        """
        assert isinstance(tax, wshop.core.models.Tax)
        assert isinstance(name, six.text_type)
        assert isinstance(amount, wshop.utils.money.Money)
        assert isinstance(base_amount, wshop.utils.money.Money)
        self.tax = tax
        self.name = name
        self.amount = amount
        self.base_amount = base_amount

    def __repr__(self):
        return '%s(%r, %r, %r, %r)' % (
            type(self).__name__,
            self.tax, self.name, self.amount, self.base_amount)
