# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from wshop.admin.forms import WshopAdminForm
from wshop.core.models import CustomCarrier, CustomPaymentProcessor


class CustomCarrierForm(WshopAdminForm):
    class Meta:
        model = CustomCarrier
        exclude = ("identifier", )


class CustomPaymentProcessorForm(WshopAdminForm):
    class Meta:
        model = CustomPaymentProcessor
        exclude = ("identifier", )
