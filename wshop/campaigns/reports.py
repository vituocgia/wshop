# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from babel.dates import format_date
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from wshop.admin.forms.fields import Select2MultipleField
from wshop.campaigns.models.campaigns import Coupon, CouponUsage
from wshop.default_reports.forms import OrderReportForm
from wshop.default_reports.mixins import OrderReportMixin
from wshop.reports.report import WshopReportBase
from wshop.utils.i18n import get_current_babel_locale


class CouponsUsageForm(OrderReportForm):
    coupon = Select2MultipleField(label=_("Coupon"),
                                  model=Coupon,
                                  required=False,
                                  help_text=_("Filter report results by coupon."))

    def __init__(self, *args, **kwargs):
        super(CouponsUsageForm, self).__init__(*args, **kwargs)

        if self.data and "coupon" in self.data:
            coupon = Coupon.objects.filter(pk__in=self.data.getlist("coupon"))
            self.fields["coupon"].initial = coupon
            self.fields["coupon"].widget.choices = [(obj.pk, obj.code) for obj in coupon]


class CouponsUsageReport(OrderReportMixin, WshopReportBase):
    identifier = "coupons-usage"
    title = _("Coupons Usage")
    filename_template = "coupons-usage-%(time)s"
    form_class = CouponsUsageForm

    schema = [
        {"key": "date", "title": _("Date")},
        {"key": "coupon", "title": _("Coupon code")},
        {"key": "order", "title": _("Order")},
        {"key": "taxful_total", "title": _("Taxful total")},
        {"key": "taxful_subtotal", "title": _("Taxful subtotal")},
        {"key": "total_discount", "title": _("Total discount")},
    ]

    def get_objects(self):
        filters = Q(order__in=super(CouponsUsageReport, self).get_objects())

        if self.options.get("coupon"):
            filters &= Q(coupon__in=self.options["coupon"])

        return CouponUsage.objects.filter(filters).order_by("order__order_date")

    def get_data(self, **kwargs):
        data = []
        coupons_usages = self.get_objects()

        for coupon_usage in coupons_usages:
            total_discount = self.shop.create_price(0)
            for discount in coupon_usage.order.lines.discounts():
                total_discount += discount.taxful_price

            data.append({
                "date": format_date(coupon_usage.order.order_date, locale=get_current_babel_locale()),
                "coupon": coupon_usage.coupon.code,
                "order": coupon_usage.order,
                "taxful_total": coupon_usage.order.taxful_total_price.as_rounded().value,
                "taxful_subtotal": (coupon_usage.order.taxful_total_price - total_discount).as_rounded().value,
                "total_discount": total_discount.as_rounded().value
            })

        return self.get_return_data(data)
