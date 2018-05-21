# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.core.urlresolvers import reverse

from wshop.testing.factories import get_default_shop
from wshop.testing.themes import (
    WshopTestingTheme, WshopTestingThemeWithCustomBase
)
from wshop.xtheme.testing import override_current_theme_class
from wshop_tests.utils import SmartClient


@pytest.mark.django_db
def test_theme_without_default_template_dir():
    with override_current_theme_class(WshopTestingTheme, get_default_shop()):
        c = SmartClient()
        soup = c.soup(reverse("wshop:index"))
        assert "Simple base for themes to use" not in soup
        assert "Welcome to test Wshop!" in soup.find("div", {"class": "page-content"}).text


@pytest.mark.django_db
def test_theme_with_default_template_dir():
    get_default_shop()
    with override_current_theme_class(WshopTestingThemeWithCustomBase, get_default_shop()):
        c = SmartClient()
        soup = c.soup(reverse("wshop:index"))
        assert "Simple base for themes to use" in soup.find("h1").text
        assert "Welcome to test Wshop!" in soup.find("h1").text
