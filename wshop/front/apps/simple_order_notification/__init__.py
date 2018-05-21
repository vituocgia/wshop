# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class SimpleOrderNotificationAppConfig(AppConfig):
    name = "wshop.front.apps.simple_order_notification"
    verbose_name = "Wshop Frontend - Simple Order Notification"
    label = "wshop_front.simple_order_notification"

    provides = {
        "admin_module": [
            "wshop.front.apps.simple_order_notification.admin_module:SimpleOrderNotificationModule",
        ]
    }


default_app_config = "wshop.front.apps.simple_order_notification.SimpleOrderNotificationAppConfig"
