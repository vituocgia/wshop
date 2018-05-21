# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from wshop.admin.forms import WshopAdminForm

from .models import (
    CarrierWithCheckoutPhase, PaymentWithCheckoutPhase, PseudoPaymentProcessor
)


class PseudoPaymentProcessorForm(WshopAdminForm):
    class Meta:
        model = PseudoPaymentProcessor
        exclude = ["identifier"]


class PaymentWithCheckoutPhaseForm(WshopAdminForm):
    class Meta:
        model = PaymentWithCheckoutPhase
        exclude = ["identifier"]


class CarrierWithCheckoutPhaseForm(WshopAdminForm):
    class Meta:
        model = CarrierWithCheckoutPhase
        exclude = ["identifier"]
