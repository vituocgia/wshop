# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from wshop import configuration
from wshop.admin.form_part import FormPart, TemplatedFormDef
from wshop.front.checkout.methods import (
    PAYMENT_METHOD_REQUIRED_CONFIG_KEY, SHIPPING_METHOD_REQUIRED_CONFIG_KEY
)


class CheckoutConfigurationForm(forms.Form):
    shipping_method_required = forms.BooleanField(
        required=False,
        label=_("Require shipping method"),
        help_text=_("Whether to require the shipping method in checkout phases.")
    )
    payment_method_required = forms.BooleanField(
        required=False,
        label=_("Require payment method"),
        help_text=_("Whether to require the payment method in checkout phases.")
    )


class CheckoutShopFormPart(FormPart):
    priority = 8
    name = "checkout_config"
    form = CheckoutConfigurationForm

    def get_form_defs(self):
        if not self.object.pk:
            return
        initial = {
            "shipping_method_required": configuration.get(self.object, SHIPPING_METHOD_REQUIRED_CONFIG_KEY, True),
            "payment_method_required": configuration.get(self.object, PAYMENT_METHOD_REQUIRED_CONFIG_KEY, True)
        }
        yield TemplatedFormDef(
            name=self.name,
            form_class=self.form,
            template_name="wshop/front/admin/checkout.jinja",
            required=False,
            kwargs={"initial": initial}
        )

    def form_valid(self, form):
        data = form[self.name].cleaned_data
        configuration.set(self.object, SHIPPING_METHOD_REQUIRED_CONFIG_KEY, data.get("shipping_method_required", False))
        configuration.set(self.object, PAYMENT_METHOD_REQUIRED_CONFIG_KEY, data.get("payment_method_required", False))