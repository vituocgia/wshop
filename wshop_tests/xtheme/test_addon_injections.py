# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from wshop.apps.provides import override_provides
from wshop.testing.factories import get_default_shop
from wshop.xtheme.resources import add_resource, InlineScriptResource
from wshop.xtheme.testing import override_current_theme_class
from wshop_tests.xtheme.utils import get_jinja2_engine, get_request


def add_test_injection(context, content):
    add_resource(context, "body_end", InlineScriptResource("window.injectedFromAddon=true;"))


@pytest.mark.django_db
def test_simple_addon_injection():
    request = get_request(edit=False)
    request.shop = get_default_shop()
    jeng = get_jinja2_engine()
    template = jeng.get_template("resinject.jinja")

    with override_current_theme_class():
        with override_provides(
                "xtheme_resource_injection", ["wshop_tests.xtheme.test_addon_injections:add_test_injection",]):
            # TestInjector should add alert to end of the body for every request
            output = template.render(request=request)
            head, body = output.split("</head>", 1)
            assert "window.injectedFromAddon=true;" in body
