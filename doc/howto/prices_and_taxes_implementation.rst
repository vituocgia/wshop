Implementation of Prices and Taxes in Wshop
===========================================

This document describes deeper details about price and tax
implementation in Wshop from a developer's point of view.  To understand
the basics, please read :doc:`../ref/prices_and_taxes` first.

.. _price-tax-types:

Types Used for Prices and Taxes
-------------------------------

`~wshop.utils.money.Money`

  Used to represent money amounts (that are not prices).  It is
  basically a `~decimal.Decimal` number with a currency.

`~wshop.core.pricing.Price`

  Used to represent prices. `Price` is a `~wshop.utils.money.Money` with
  an `includes_tax` property.  It has has two subclasses:
  `~wshop.core.pricing.TaxfulPrice` and
  `~wshop.core.pricing.TaxlessPrice`.

  There should usually be no need to create prices directly with these
  classes; see :ref:`creating-prices`.

`~wshop.core.pricing.Priceful`

  An interface for accessing the price information of a product, order
  line, basket line, or whatever.  See :ref:`accessing-prices`.

`~wshop.core.pricing.PriceInfo`

  A class for describing an item's price information.

`~wshop.core.pricing.PricingModule`

  An interface for querying prices of products.

`~wshop.core.pricing.PricingContext`

  A container for variables that affect pricing.  Pricing modules may
  subclass this.

`~wshop.core.pricing.PricingContextable`

  An interface for objects that can be converted to a pricing context.
  Instances of `PricingContext` or `~django.http.HttpRequest` satisfy
  this interface.

`~wshop.core.taxing.LineTax`

  An interface for describing a calculated tax of a line in order or
  basket.  Has a reference to the line and to the applied tax and the
  calculated amount of tax. One line could have several taxes applied,
  each is presented with a separate `LineTax`.

`~wshop.core.taxing.SourceLineTax`

  A container for a calculated tax of a
  `~wshop.core.order_creator.SourceLine` (or
  `~wshop.front.basket.objects.BasketLine`).  Implements the `LineTax`
  interface.

`~wshop.core.models.OrderLineTax`

  A Django model for persistently storing the calculated tax of an
  `~wshop.core.models.OrderLine`.  Implements the `LineTax` interface.

`~wshop.core.models.Tax`

  A Django model for a tax with name, code, and percentage rate or fixed
  amount.  Fixed amounts are not yet supported.

  .. TODO:: Fix this when fixed amounts are supported.

`~wshop.core.taxing.TaxableItem`

  An interface for items that can be taxed.  Implemented by
  `~wshop.core.models.Product`, `~wshop.core.models.ShippingMethod`,
  `~wshop.core.models.PaymentMethod` and
  `~wshop.core.order_creator.SourceLine`.

`~wshop.core.models.TaxClass`

  A Django model for a tax class.  Taxable items (e.g. products, methods
  or lines) are grouped to tax classes to make it possible to have
  different taxation rules for different groups of items.

`~wshop.core.models.CustomerTaxGroup`

  A Django model for grouping customers to make it possible to have
  different taxation rules for different groups of customers.  Wshop
  assigns separate `CustomerTaxGroup`s for a
  `~wshop.core.models.PersonContact` and a
  `~wshop.core.models.CompanyContact` by default.

`~wshop.core.taxing.TaxModule`

  An interface for calculating the taxes of an
  `~wshop.core.order_creator.OrderSource` or any `TaxableItem`.  The
  Wshop Base distribution ships a concrete implementation of a
  `TaxModule` called `~wshop.default_tax.module.DefaultTaxModule`.  It
  is a based on a table of tax rules (saved with
  `~wshop.default_tax.models.TaxRule` model).  See
  :ref:`default-tax-module`.  Used `TaxModule` can be changed with
  `~wshop.core.settings.WSHOP_TAX_MODULE` setting.

`~wshop.core.taxing.TaxedPrice`

  A type to represent the return value of tax calculation.  Contains a
  pair of prices, `TaxfulPrice` and `TaxlessPrice`, of which one is the
  original price before the calculation and the other is the calculated
  price. Also contains a list of the applied taxes.  `TaxedPrice` is the
  return type of `~wshop.core.taxing.TaxModule.get_taxed_price_for`
  method in the `TaxModule` interface.

`~wshop.core.taxing.TaxingContext`

  A container for variables that affect taxing, such as customer tax
  group, customer tax number, location (country, postal code, etc.).
  Used in the `TaxModule` interface. Note: This is *not* usually
  subclassed.

.. _creating-prices:

Creating Prices
---------------

When implementing a `~wshop.core.pricing.PricingModule` or another
module that has to create prices, use the `Shop.create_price
<wshop.core.models.Shop.create_price>` method.  It makes sure that all
prices have the same :ref:`price unit <price-unit>`.

.. _accessing-prices:

Accessing Prices of Product or Line
-----------------------------------

There is a `~wshop.core.pricing.Priceful` interface for accessing
prices.  It is implemented by `~wshop.core.models.OrderLine` and
`~wshop.core.order_creator.SourceLine`,
`~wshop.front.basket.objects.BasketLine`, and
`~wshop.core.pricing.PriceInfo` which is returned e.g. by
`~wshop.core.models.Product.get_price_info` method.
