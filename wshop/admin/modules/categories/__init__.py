# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import six
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from filer.models import File

from wshop.admin.base import AdminModule, MenuEntry, SearchResult
from wshop.admin.menu import PRODUCTS_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls, get_model_url
)
from wshop.admin.views.home import HelpBlockCategory, SimpleHelpBlock
from wshop.core.models import Category


class CategoryModule(AdminModule):
    name = _("Categories")
    category = _("Products")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="wshop_admin:category.list", category=PRODUCTS_MENU_CATEGORY)

    def get_urls(self):
        return [
            admin_url(
                "^categories/(?P<pk>\d+)/copy-visibility/$",
                "wshop.admin.modules.categories.views.CategoryCopyVisibilityView",
                name="category.copy_visibility",
                permissions=get_default_model_permissions(Category)
            ),
            admin_url(
                "^categories/(?P<pk>\d+)/delete/$",
                "wshop.admin.modules.categories.views.CategoryDeleteView",
                name="category.delete",
                permissions=get_default_model_permissions(Category)
            ),
        ] + get_edit_and_list_urls(
            url_prefix="^categories",
            view_template="wshop.admin.modules.categories.views.Category%sView",
            name_template="category.%s",
            permissions=get_default_model_permissions(Category),
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Categories"), icon="fa fa-sitemap",
                url="wshop_admin:category.list", category=PRODUCTS_MENU_CATEGORY, ordering=2
            )
        ]

    def get_search_results(self, request, query):
        minimum_query_length = 3
        if len(query) >= minimum_query_length:
            categories = Category.objects.filter(
                Q(translations__name__icontains=query) |
                Q(identifier__icontains=query)
            ).distinct().order_by("tree_id", "lft")
            for i, category in enumerate(categories[:10]):
                relevance = 100 - i
                yield SearchResult(
                    text=six.text_type(category),
                    url=get_model_url(category),
                    category=self.category,
                    relevance=relevance
                )

    def get_help_blocks(self, request, kind):
        yield SimpleHelpBlock(
            text=_("Add a product category to organize your products"),
            actions=[{
                "text": _("New category"),
                "url": get_model_url(Category, "new")
            }],
            icon_url="wshop_admin/img/category.png",
            category=HelpBlockCategory.PRODUCTS,
            priority=1,
            done=Category.objects.filter(shops=request.shop).exists() if kind == "setup" else False
        )

    def get_required_permissions(self):
        return get_default_model_permissions(Category) | get_default_model_permissions(File)

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Category, "wshop_admin:category", object, kind)
