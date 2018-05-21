# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from wshop.apps import AppConfig


class WshopNotifyAppConfig(AppConfig):
    name = "wshop.notify"
    verbose_name = "Wshop Notification Framework"
    label = "wshop_notify"
    provides = {
        "notify_condition": [
            "wshop.notify.conditions:LanguageEqual",
            "wshop.notify.conditions:BooleanEqual",
            "wshop.notify.conditions:IntegerEqual",
            "wshop.notify.conditions:TextEqual",
            "wshop.notify.conditions:Empty",
            "wshop.notify.conditions:NonEmpty",
        ],
        "notify_action": [
            "wshop.notify.actions:SetDebugFlag",
            "wshop.notify.actions:AddOrderLogEntry",
            "wshop.notify.actions:SendEmail",
            "wshop.notify.actions:AddNotification",
        ],
        "notify_event": [],
        "admin_module": [
            "wshop.notify.admin_module:NotifyAdminModule",
        ]
    }


default_app_config = "wshop.notify.WshopNotifyAppConfig"
