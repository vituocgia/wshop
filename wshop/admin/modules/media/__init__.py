# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _
from filer.models import File

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import CONTENT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url


class MediaModule(AdminModule):
    """
    A module for handling site media.
    Basically a frontend for the Django-Filer app.
    """

    name = _("Media")

    def get_urls(self):
        return [
            admin_url(
                "^media/$",
                "wshop.admin.modules.media.views.MediaBrowserView",
                name="media.browse",
                permissions=get_default_model_permissions(File),
            ),
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(File)

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Media browser"),
                icon="fa fa-folder-open",
                url="wshop_admin:media.browse",
                category=CONTENT_MENU_CATEGORY,
                subcategory="other",
                ordering=2
            ),
        ]
