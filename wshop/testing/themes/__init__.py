# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.utils.translation import ugettext_lazy as _

from wshop.xtheme import Theme


class WshopTestingTheme(Theme):
    identifier = "wshop_testing"
    name = _("Wshop Testing Theme")
    author = "Wshop Team"
    template_dir = "wshop_testing"

    plugins = [__name__ + ".plugins.HighlightTestPlugin"]


class WshopTestingThemeWithCustomBase(WshopTestingTheme):
    identifier = "wshop_testing_with_custom_base_template"
    name = _("Wshop Testing Theme With Custom Base Template")
    default_template_dir = "default_templates"
