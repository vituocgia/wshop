# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.template import engines
from django.utils.translation import ugettext_lazy as _
from django_jinja.backend import Jinja2

from wshop.admin.base import AdminModule, MenuEntry, Notification
from wshop.admin.menu import CONTENT_MENU_CATEGORY
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import admin_url
from wshop.admin.views.home import HelpBlockCategory, SimpleHelpBlock
from wshop.xtheme._theme import get_current_theme
from wshop.xtheme.engine import XthemeEnvironment
from wshop.xtheme.models import ThemeSettings


class XthemeAdminModule(AdminModule):
    """
    Admin module for Xtheme.

    Allows theme activation/deactivation and further configuration.
    """
    name = _("Wshop Extensible Theme Engine")
    breadcrumbs_menu_entry = MenuEntry(_("Themes"), "wshop_admin:xtheme.config", category=CONTENT_MENU_CATEGORY)

    def get_urls(self):  # doccov: ignore
        return [
            admin_url(
                "^xtheme/guide/(?P<theme_identifier>.+?)/",
                "wshop.xtheme.admin_module.views.ThemeGuideTemplateView",
                name="xtheme.guide",
                permissions=get_default_model_permissions(ThemeSettings)
            ),
            admin_url(
                "^xtheme/configure/(?P<theme_identifier>.+?)/",
                "wshop.xtheme.admin_module.views.ThemeConfigDetailView",
                name="xtheme.config_detail",
                permissions=get_default_model_permissions(ThemeSettings)
            ),
            admin_url(
                "^xtheme/",
                "wshop.xtheme.admin_module.views.ThemeConfigView",
                name="xtheme.config",
                permissions=get_default_model_permissions(ThemeSettings)
            )
        ]

    def get_menu_entries(self, request):  # doccov: ignore
        return [
            MenuEntry(
                text=_("Themes"), icon="fa fa-paint-brush",
                url="wshop_admin:xtheme.config",
                category=CONTENT_MENU_CATEGORY,
                subcategory="design",
                ordering=1
            )
        ]

    def get_help_blocks(self, request, kind):
        theme = get_current_theme(request.shop)
        if kind == "quicklink" and theme:
            yield SimpleHelpBlock(
                text=_("Customize the look and feel of your shop"),
                actions=[{
                    "text": _("Customize theme"),
                    "url": reverse("wshop_admin:xtheme.config_detail", kwargs={"theme_identifier": theme.identifier})
                }],
                priority=200,
                category=HelpBlockCategory.STOREFRONT,
                icon_url="xtheme/theme.png"
            )

    def get_required_permissions(self):
        return get_default_model_permissions(ThemeSettings)

    def get_notifications(self, request):
        try:
            engine = engines["jinja2"]
        except KeyError:
            engine = None

        if engine and isinstance(engine, Jinja2):  # The engine is what we expect...
            if isinstance(engine.env, XthemeEnvironment):  # ... and it's capable of loading themes...
                if not get_current_theme(request.shop):  # ... but there's no theme active?!
                    # Panic!
                    yield Notification(
                        text=_("No theme is active. Click here to activate one."),
                        title=_("Theming"),
                        url="wshop_admin:xtheme.config"
                    )
