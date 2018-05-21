# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from filer.models import File

from wshop.admin.base import AdminModule, MenuEntry
from wshop.admin.menu import CONTENT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from wshop.core.models import Product
from wshop.front.apps.carousel.models import Carousel


class CarouselModule(AdminModule):
    name = _("Carousels")
    breadcrumbs_menu_entry = MenuEntry(text=name, url="wshop_admin:carousel.list", category=CONTENT_MENU_CATEGORY)

    def get_urls(self):
        return get_edit_and_list_urls(
            url_prefix="^carousels",
            view_template="wshop.front.apps.carousel.admin_module.views.Carousel%sView",
            name_template="carousel.%s",
            permissions=get_default_model_permissions(Carousel)
        ) + [
            admin_url(
                "^carousel/(?P<pk>\d+)/delete/$",
                "wshop.front.apps.carousel.admin_module.views.CarouselDeleteView",
                name="carousel.delete",
                permissions=get_default_model_permissions(Carousel)
            ),
        ]

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=self.name,
                icon="fa fa-image",
                url="wshop_admin:carousel.list",
                category=CONTENT_MENU_CATEGORY,
                subcategory="elements"
            )
        ]

    def get_required_permissions(self):
        return (
            get_default_model_permissions(Carousel) |
            get_default_model_permissions(File) |
            get_default_model_permissions(Product)
        )

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Carousel, "wshop_admin:carousel", object, kind)
