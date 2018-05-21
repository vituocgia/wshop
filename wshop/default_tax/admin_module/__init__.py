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
from wshop.admin.menu import SETTINGS_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import derive_model_url, get_edit_and_list_urls
from wshop.default_tax.models import TaxRule


class TaxRulesAdminModule(AdminModule):
    name = _("Tax Rules")
    breadcrumbs_menu_entry = MenuEntry(name, "wshop_admin:default_tax.tax_rule.list")

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^default-tax/rules",
            view_template="wshop.default_tax.admin_module.views.TaxRule%sView",
            name_template="default_tax.tax_rule.%s",
            permissions=get_default_model_permissions(TaxRule)
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Tax Rules"), icon="fa fa-file-text",
                url="wshop_admin:default_tax.tax_rule.list",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="taxes",
                ordering=4, aliases=[_("Show tax rules")]
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(TaxRule)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(TaxRule, "wshop_admin:default_tax.tax_rule", object, kind)
