# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import REPORTS_MENU_CATEGORY
from wshop.admin.utils.urls import admin_url


class ReportsAdminModule(AdminModule):
    name = _("Reports")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="wshop_admin:reports.list")

    def get_urls(self):
        return [
            admin_url("^reports/$", "wshop.reports.admin_module.views.ReportView", name="reports.list")
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-image",
                url="wshop_admin:reports.list",
                category=REPORTS_MENU_CATEGORY
            )
        ]
