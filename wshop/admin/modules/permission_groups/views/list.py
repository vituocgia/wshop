# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.contrib.auth.models import Group as PermissionGroup
from django.utils.translation import ugettext_lazy as _

from wshop.admin.toolbar import NewActionButton, SettingsActionButton, Toolbar
from wshop.admin.utils.picotable import Column, TextFilter
from wshop.admin.utils.views import PicotableListView


class PermissionGroupListView(PicotableListView):
    model = PermissionGroup
    default_columns = [
        Column(
            "name",
            _(u"Name"),
            sort_field="name",
            display="name",
            filter_config=TextFilter(filter_field="name", placeholder=_("Filter by name..."))
        ),
    ]

    def get_context_data(self, **kwargs):
        context = super(PermissionGroupListView, self).get_context_data(**kwargs)
        context["title"] = _("Permission Groups")
        if self.request.user.is_superuser:
            settings_button = SettingsActionButton.for_model(self.model, return_url="permission_group")
        else:
            settings_button = None
        context["toolbar"] = Toolbar([
            NewActionButton("wshop_admin:permission_group.new", text=_("Create new Permission Group")),
            settings_button
        ])
        return context