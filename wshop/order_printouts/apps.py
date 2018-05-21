# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import wshop.apps


class AppConfig(wshop.apps.AppConfig):
    name = "wshop.order_printouts"
    verbose_name = _("Order printouts")
    label = "wshop_order_printouts"

    provides = {
        "admin_module": [
            "wshop.order_printouts.admin_module:PrintoutsAdminModule"
        ],
        "admin_order_section": [
            "wshop.order_printouts.admin_module.section:PrintoutsSection"
        ],
    }
