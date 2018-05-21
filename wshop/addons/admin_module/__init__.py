# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import ADDONS_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url
from wshop.core.models import Shop


class AddonModule(AdminModule):
    name = _("Addons")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="wshop_admin:addon.list")

    def get_urls(self):
        return [
            admin_url(
                "^addons/$",
                "wshop.addons.admin_module.views.AddonListView",
                name="addon.list",
                permissions=get_default_model_permissions(Shop)
            ),
            admin_url(
                "^addons/add/$",
                "wshop.addons.admin_module.views.AddonUploadView",
                name="addon.upload",
                permissions=get_default_model_permissions(Shop)
            ),
            admin_url(
                "^addons/add/confirm/$",
                "wshop.addons.admin_module.views.AddonUploadConfirmView",
                name="addon.upload_confirm",
                permissions=get_default_model_permissions(Shop)
            ),
            admin_url(
                "^addons/reload/$",
                "wshop.addons.admin_module.views.ReloadView",
                name="addon.reload",
                permissions=get_default_model_permissions(Shop)
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Addons"),
                icon="fa fa-puzzle-piece",
                url="wshop_admin:addon.list",
                category=ADDONS_MENU_CATEGORY
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(Shop)
