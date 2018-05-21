# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from filer.models import File

from wshop.admin.base import AdminModule, MenuEntry, SearchResult
from wshop.admin.menu import STOREFRONT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls, get_model_url
)
from wshop.admin.views.home import SimpleHelpBlock
from wshop.core.models import Shop


class ShopModule(AdminModule):
    name = _("Shops")
    breadcrumbs_menu_entry = MenuEntry(name, url="wshop_admin:shop.list")

    def get_urls(self):
        return [
            admin_url(
                "^shops/(?P<pk>\d+)/enable/$",
                "wshop.admin.modules.shops.views.ShopEnablerView",
                name="shop.enable",
                permissions=get_default_model_permissions(Shop)
            ),
            admin_url(
                "^shops/(?P<pk>\d+)/select/$",
                "wshop.admin.modules.shops.views.ShopSelectView",
                name="shop.select",
                permissions=get_default_model_permissions(Shop)
            ),
        ] + get_edit_and_list_urls(
            url_prefix="^shops",
            view_template="wshop.admin.modules.shops.views.Shop%sView",
            name_template="shop.%s",
            permissions=get_default_model_permissions(Shop)
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-house",
                url="wshop_admin:shop.list",
                category=STOREFRONT_MENU_CATEGORY,
                subcategory="settings",
                ordering=4
            ),
        ]

    def get_help_blocks(self, request, kind):
        if kind == "setup":
            shop = request.shop
            yield SimpleHelpBlock(
                text=_("Add a logo to make your store stand out"),
                actions=[{
                    "text": _("Add logo"),
                    "url": self.get_model_url(shop, "edit"),
                    "hash": "#shop-images-section"
                }],
                icon_url="wshop_admin/img/logo-icon.svg",
                done=shop.logo
            )

    def get_required_permissions(self):
        return get_default_model_permissions(Shop) | get_default_model_permissions(File)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Shop, "wshop_admin:shop", object, kind)

    def get_search_results(self, request, query):
        if not settings.WSHOP_ENABLE_MULTIPLE_SHOPS:
            return

        minimum_query_length = 3
        if len(query) >= minimum_query_length:
            shops = Shop.objects.get_for_user(request.user).filter(translations__name__icontains=query)
            for i, shop in enumerate(shops[:10]):
                relevance = 100 - i
                yield SearchResult(
                    text=(_('Set "{}" as the active shop')).format(shop.name),
                    url=get_model_url(shop, "select"),
                    category=(_("Available Shops [currently active: {}]")).format(request.shop.name),
                    relevance=relevance
                )