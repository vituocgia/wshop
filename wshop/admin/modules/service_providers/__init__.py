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
from wshop.admin.menu import STOREFRONT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from wshop.core.models import ServiceProvider


class ServiceProviderModule(AdminModule):
    name = _("Service Providers")
    category = _("Payment and Shipping")

    def get_urls(self):
        return [
            admin_url(
                "^service_provider/(?P<pk>\d+)/delete/$",
                "wshop.admin.modules.service_providers.views.ServiceProviderDeleteView",
                name="service_provider.delete",
                permissions=["wshop.delete_serviceprovider"]
            )
        ] + get_edit_and_list_urls(
            url_prefix="^service_provider",
            view_template="wshop.admin.modules.service_providers.views.ServiceProvider%sView",
            name_template="service_provider.%s",
            permissions=get_default_model_permissions(ServiceProvider)
        )

    def get_menu_category_icons(self):
        return {self.category: "fa fa-cubes"}

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-truck",
                url="wshop_admin:service_provider.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="payment_shipping",
                ordering=3
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(ServiceProvider)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(ServiceProvider, "wshop_admin:service_provider", object, kind)
