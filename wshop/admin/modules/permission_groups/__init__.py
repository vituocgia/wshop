# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.contrib.auth.models import Group as PermissionGroup
from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import STOREFRONT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import derive_model_url, get_edit_and_list_urls


class PermissionGroupModule(AdminModule):
    name = _("Permission Groups")
    breadcrumbs_menu_entry = MenuEntry(name, url="wshop_admin:permission_group.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^permission-groups",
            view_template="wshop.admin.modules.permission_groups.views.PermissionGroup%sView",
            name_template="permission_group.%s",
            permissions=get_default_model_permissions(PermissionGroup),
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-users",
                url="wshop_admin:permission_group.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="other_settings",
                ordering=3
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(PermissionGroup)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(PermissionGroup, "wshop_admin:permission_group", object, kind)
