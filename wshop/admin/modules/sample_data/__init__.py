# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

import os

from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule, MenuEntry, Notification
from wshop.admin.menu import SETTINGS_MENU_CATEGORY
from wshop.admin.modules.sample_data import manager as sample_manager
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url
from wshop.core.models import Shop
from wshop.core.settings_provider import WshopSettings

SAMPLE_BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAMPLE_IMAGES_BASE_DIR = os.path.join(SAMPLE_BASE_DIR, "sample_data/images")


class SampleDataAdminModule(AdminModule):
    def get_urls(self):
        return [
            admin_url(
                "^sample_data/$",
                "wshop.admin.modules.sample_data.views.ConsolidateSampleObjectsView",
                name="sample_data",
                permissions=get_default_model_permissions(Shop)
            )
        ]

    def get_menu_entries(self, request):
        # not supported
        if WshopSettings.get_setting("WSHOP_ENABLE_MULTIPLE_SHOPS"):
            return []

        return [
            MenuEntry(
                text="Sample Data",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="data_transfer",
                url="wshop_admin:sample_data",
                icon="fa fa-star"
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(Shop)

    def get_notifications(self, request):
        """ Injects a message to the user and also a notification """
        # multi-shop not supported
        if not WshopSettings.get_setting("WSHOP_ENABLE_MULTIPLE_SHOPS"):
            # there would be only sample data for single-shops envs
            shop = Shop.objects.first()

            if sample_manager.has_installed_samples(shop):
                messages.warning(request, _('There is sample data installed. '
                                            'Access "Settings > Sample Data" for more information.'))

                yield Notification(
                    _("There is sample data installed. Click here to consolidate or delete them."),
                    title=_("Sample Data"),
                    kind="warning",
                    url="wshop_admin:sample_data"
                )
