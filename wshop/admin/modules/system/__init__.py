# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry, Notification
from wshop.admin.menu import SETTINGS_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url
from wshop.core.models import Shop
from wshop.core.telemetry import (
    is_in_grace_period, is_opt_out, is_telemetry_enabled
)


class SystemModule(AdminModule):
    name = _("System")

    def get_urls(self):
        return [
            admin_url(
                "^system/telemetry/$",
                "wshop.admin.modules.system.views.telemetry.TelemetryView",
                name="telemetry",
                permissions=get_default_model_permissions(Shop)
            ),
        ]

    def get_menu_entries(self, request):
        return [e for e in [
            MenuEntry(
                text=_("Telemetry"),
                icon="fa fa-tachometer",
                url="wshop_admin:telemetry",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="other_settings",
            ) if is_telemetry_enabled() else None,
        ] if e]

    def get_required_permissions(self):
        return get_default_model_permissions(Shop)

    def get_notifications(self, request):
        if is_telemetry_enabled() and is_in_grace_period() and not is_opt_out():
            yield Notification(
                _("Statistics will be periodically sent to Wshop.com after 24 hours. Click here for more information."),
                title=_("Telemetry"),
                kind="info",
                url="wshop_admin:telemetry"
            )
