# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.testing.factories import get_default_shop
from wshop.testing.themes import WshopTestingTheme
from wshop.testing.themes.plugins import HighlightTestPlugin
from wshop.xtheme import templated_plugin_factory, TemplatedPlugin
from wshop.xtheme.testing import override_current_theme_class
from wshop_tests.utils import printable_gibberish
from wshop_tests.xtheme.utils import get_jinja2_engine, plugin_override


def test_plugin_choices():
    with plugin_override():
        theme = WshopTestingTheme(shop=get_default_shop())
        choice_identifiers = set()
        for identifier, data in theme.get_all_plugin_choices():
            for choice in data:
                choice_identifiers.add(choice[0])
        assert choice_identifiers == set(("inject", "text", HighlightTestPlugin.identifier))


def test_templated_plugin():
    jeng = get_jinja2_engine()

    my_plugin_class = templated_plugin_factory("MyPlugin", "templated_plugin.jinja",
        inherited_variables=("name",),
        config_copied_variables=("greeting",),
        engine=jeng
    )
    top_context = {
        "name": printable_gibberish(),
    }
    config = {
        "greeting": "Good day"
    }
    plugin = my_plugin_class(config=config)
    assert isinstance(plugin, TemplatedPlugin)
    with override_current_theme_class(None):
        rendered_content = plugin.render(top_context)
        expected_content = "Good day %s" % top_context["name"]
        assert rendered_content == expected_content
