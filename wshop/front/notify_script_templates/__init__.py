# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from .generics import (
    OrderConfirmationEmailScriptTemplate, PaymentCreatedEmailScriptTemplate,
    RefundCreatedEmailScriptTemplate, ShipmentCreatedEmailScriptTemplate,
    ShipmentDeletedEmailScriptTemplate
)

__all__ = [
    "OrderConfirmationEmailScriptTemplate",
    "PaymentCreatedEmailScriptTemplate",
    "RefundCreatedEmailScriptTemplate",
    "ShipmentDeletedEmailScriptTemplate",
    "ShipmentCreatedEmailScriptTemplate"
]
