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
from wshop.admin.menu import CAMPAIGNS_MENU_CATEGORY
from wshop.admin.utils.permissions import (
    get_default_model_permissions, get_permissions_from_urls
)
from wshop.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from wshop.admin.views.home import HelpBlockCategory, SimpleHelpBlock
from wshop.campaigns.models import BasketCampaign, CatalogCampaign, Coupon


class CampaignAdminModule(AdminModule):
    name = _(u"Campaigns")

    def get_urls(self):
        basket_campaign_urls = get_edit_and_list_urls(
            url_prefix="^campaigns/basket",
            view_template="wshop.campaigns.admin_module.views.BasketCampaign%sView",
            name_template="basket_campaign.%s",
            permissions=get_default_model_permissions(BasketCampaign)
        )

        coupon_urls = get_edit_and_list_urls(
            url_prefix="^campaigns/coupons",
            view_template="wshop.campaigns.admin_module.views.Coupon%sView",
            name_template="coupon.%s",
            permissions=get_default_model_permissions(Coupon)
        )

        return basket_campaign_urls + coupon_urls + get_edit_and_list_urls(
            url_prefix="^campaigns/catalog",
            view_template="wshop.campaigns.admin_module.views.CatalogCampaign%sView",
            name_template="catalog_campaign.%s",
            permissions=get_default_model_permissions(CatalogCampaign)
        )

    def get_menu_category_icons(self):
        return {self.name: "fa fa-bullhorn"}

    def get_menu_entries(self, request):
        category = CAMPAIGNS_MENU_CATEGORY
        return [
            MenuEntry(
                text=_("Catalog Campaigns"), icon="fa fa-file-text",
                url="wshop_admin:catalog_campaign.list",
                category=category, ordering=1, aliases=[_("Show Catalog Campaigns")]
            ),
            MenuEntry(
                text=_("Basket Campaigns"), icon="fa fa-file-text",
                url="wshop_admin:basket_campaign.list",
                category=category, ordering=2, aliases=[_("Show Basket Campaigns")]
            ),
            MenuEntry(
                text=_("Coupons"), icon="fa fa-file-text",
                url="wshop_admin:coupon.list",
                category=category, ordering=3, aliases=[_("Show Coupons")]
            )
        ]

    def get_help_blocks(self, request, kind):
        if kind == "quicklink":
            yield SimpleHelpBlock(
                text=_("Set up a sales campaign"),
                actions=[{
                    "text": _("New basket campaign"),
                    "url": self.get_model_url(BasketCampaign, "new")
                }, {
                    "text": _("New catalog campaign"),
                    "url": self.get_model_url(CatalogCampaign, "new")
                }, {
                    "text": _("New coupon"),
                    "url": self.get_model_url(Coupon, "new")
                }],
                priority=1,
                category=HelpBlockCategory.CAMPAIGNS,
                icon_url="wshop/campaigns/img/campaign.png"
            )

    def get_required_permissions(self):
        return get_permissions_from_urls(self.get_urls())

    def get_model_url(self, object, kind, shop=None):
        if not hasattr(object, "admin_url_suffix"):
            return super(CampaignAdminModule, self).get_model_url(object, kind)
        admin_url = "wshop_admin:%s" % object.admin_url_suffix
        return derive_model_url(type(object), admin_url, object, kind)
