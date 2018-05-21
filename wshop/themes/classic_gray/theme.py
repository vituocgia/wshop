# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

import django.conf
from django import forms
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from wshop.xtheme import Theme


class ClassicGrayTheme(Theme):
    identifier = "wshop.themes.classic_gray"
    name = "Wshop Classic Gray Theme"
    author = "Wshop Team"
    template_dir = "classic_gray"

    fields = [
        ("show_welcome_text", forms.BooleanField(required=False, initial=True, label=_("Show Frontpage Welcome Text"))),
    ]

    guide_template = "classic_gray/admin/guide.jinja"

    stylesheets = [
        {
            "identifier": "default",
            "stylesheet": "wshop/front/css/style.css",
            "name": _("Default"),
            "images": []
        },
        {
            "identifier": "midnight_blue",
            "stylesheet": "wshop/classic_gray/blue/style.css",
            "name": _("Midnight Blue"),
            "images": []
        },
        {
            "identifier": "candy_pink",
            "stylesheet": "wshop/classic_gray/pink/style.css",
            "name": _("Candy Pink"),
            "images": []
        },
    ]

    def get_view(self, view_name):
        import wshop.front.themes.views as views
        return getattr(views, view_name, None)

    def _format_cms_links(self, shop, **query_kwargs):
        if "wshop.simple_cms" not in django.conf.settings.INSTALLED_APPS:
            return
        from wshop.simple_cms.models import Page
        for page in Page.objects.visible(shop).filter(**query_kwargs):
            yield {"url": "/%s" % page.url, "text": force_text(page)}

    def get_cms_navigation_links(self, request):
        return self._format_cms_links(shop=request.shop, visible_in_menu=True)
