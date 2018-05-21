# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.core.urlresolvers import reverse
from wshop.apps.provides import override_provides
from wshop.testing.factories import get_default_shop
from wshop.xtheme.extenders import FrontMenuExtender
from wshop_tests.utils import SmartClient

class TestExtender(FrontMenuExtender):
    items = [
        {"url": "wshop:index", "title": "Test Link to Front"}
    ]

@pytest.mark.django_db
def test_extender_renders_main_menu(rf):
    get_default_shop()

    with override_provides("front_menu_extender", ["wshop_tests.xtheme.test_extenders:TestExtender"]):
        c = SmartClient()
        soup = c.soup(reverse("wshop:index"))
        link_texts = [a.text for a in soup.findAll("a")]
        assert "Test Link to Front" in link_texts
