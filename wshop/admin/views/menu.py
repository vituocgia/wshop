# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.views.generic import TemplateView


class MenuView(TemplateView):
    template_name = "wshop/admin/base/_main_menu.jinja"
