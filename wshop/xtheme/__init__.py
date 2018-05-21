# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig
from wshop.utils import update_module_attributes

from ._theme import (
    get_current_theme, get_middleware_current_theme, get_theme_by_identifier,
    get_theme_cache_key, set_current_theme, set_middleware_current_theme,
    Theme
)
from .plugins._base import Plugin, templated_plugin_factory, TemplatedPlugin

__all__ = [
    "Plugin",
    "TemplatedPlugin",
    "Theme",
    "get_current_theme",
    "get_theme_by_identifier",
    "set_current_theme",
    "templated_plugin_factory",
    "get_theme_cache_key",
    "get_middleware_current_theme",
    "set_middleware_current_theme"
]

XTHEME_GLOBAL_VIEW_NAME = "_XthemeGlobalView"


class XThemeAppConfig(AppConfig):
    name = "wshop.xtheme"
    verbose_name = "Wshop Extensible Theme Engine"
    label = "wshop_xtheme"

    provides = {
        "front_urls_pre": [__name__ + ".urls:urlpatterns"],
        "xtheme_plugin": [
            "wshop.xtheme.plugins.image:ImagePlugin",
            "wshop.xtheme.plugins.category_links:CategoryLinksPlugin",
            "wshop.xtheme.plugins.products:ProductsFromCategoryPlugin",
            "wshop.xtheme.plugins.products:ProductHighlightPlugin",
            "wshop.xtheme.plugins.products:ProductCrossSellsPlugin",
            "wshop.xtheme.plugins.snippets:SnippetsPlugin",
            "wshop.xtheme.plugins.social_media_links:SocialMediaLinksPlugin",
            "wshop.xtheme.plugins.text:TextPlugin",
        ],
        "admin_module": [
            "wshop.xtheme.admin_module:XthemeAdminModule"
        ]
    }


default_app_config = "wshop.xtheme.XThemeAppConfig"

update_module_attributes(__all__, __name__)
