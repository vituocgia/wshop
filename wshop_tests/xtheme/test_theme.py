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
from wshop.xtheme import (
    get_current_theme, get_theme_by_identifier, set_current_theme
)
from wshop.xtheme.models import ThemeSettings
from wshop.xtheme.testing import override_current_theme_class
from wshop_tests.utils import printable_gibberish
from wshop_tests.xtheme.utils import FauxTheme, FauxTheme2


@pytest.mark.django_db
def test_theme_activation():
    shop = get_default_shop()
    with override_current_theme_class():
        with override_provides("xtheme", [
            "wshop_tests.xtheme.utils:FauxTheme",
            "wshop_tests.xtheme.utils:FauxTheme2"
        ]):
            ThemeSettings.objects.all().delete()
            # ThemeSettings will be created on the fly
            theme = get_current_theme(shop)
            assert theme
            assert theme.settings_obj
            set_current_theme(FauxTheme.identifier, shop)
            assert isinstance(get_current_theme(shop), FauxTheme)
            set_current_theme(FauxTheme2.identifier, shop)
            assert isinstance(get_current_theme(shop), FauxTheme2)
            with pytest.raises(ValueError):
                set_current_theme(printable_gibberish(), shop)



@pytest.mark.django_db
def test_theme_settings_api():
    shop = get_default_shop()
    with override_provides("xtheme", [
        "wshop_tests.xtheme.utils:FauxTheme",
        "wshop_tests.xtheme.utils:FauxTheme2"
    ]):
        ThemeSettings.objects.all().delete()
        theme = get_theme_by_identifier(FauxTheme2.identifier, shop)
        theme.set_setting("foo", "bar")
        theme.set_settings(quux=[4, 8, 15, 16, 23, 42])
        theme = get_theme_by_identifier(FauxTheme2.identifier, shop)
        assert theme.get_setting("foo") == "bar"
        assert theme.get_settings() == {
            "foo": "bar",
            "quux": [4, 8, 15, 16, 23, 42]
        }
