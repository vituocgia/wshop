# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

ABOUT_US_KEY = "about_us"
PRIVACY_POLICY_KEY = "privacy_policy"
TERMS_AND_CONDITIONS_KEY = "terms_conditions"
REFUND_POLICY_KEY = "refund_policy"

CMS_PAGES = {
    ABOUT_US_KEY: {
        "name": _("About Us"),
        "template": "wshop/admin/content/data/about_us.jinja"
    },
    PRIVACY_POLICY_KEY: {
        "name": _("Privacy Policy"),
        "template": "wshop/admin/content/data/privacy_policy.jinja"
    },
    TERMS_AND_CONDITIONS_KEY: {
        "name": _("Terms and Conditions"),
        "template": "wshop/admin/content/data/terms_and_conditions.jinja"
    },
    REFUND_POLICY_KEY: {
        "name": _("Refund Policy"),
        "template": "wshop/admin/content/data/refund_policy.jinja"
    },
}

FOOTER_TEMPLATE = "wshop/admin/content/data/footer.jinja"

ORDER_CONFIRMATION = {
    "subject": _("{{ order.shop }} - Order {{ order.identifier }} Received"),
    "content_type": "html",
    "body_template": "wshop/admin/content/data/order_confirmation.jinja"
}
