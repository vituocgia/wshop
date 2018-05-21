# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.notify.base import Event, Variable
from wshop.notify.typology import Email, Model


class CompanyAccountCreated(Event):
    identifier = "company_account_created"

    contact = Variable("CompanyContact", type=Model("wshop.CompanyContact"))
    customer_email = Variable("Customer Email", type=Email)
