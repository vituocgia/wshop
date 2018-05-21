# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from wshop.apps import AppConfig


class SimpleSearchAppConfig(AppConfig):
    name = "wshop.front.apps.simple_search"
    verbose_name = "Wshop Frontend - Simple Search"
    label = "wshop_front.simple_search"

    provides = {
        "front_urls": [
            "wshop.front.apps.simple_search.urls:urlpatterns"
        ],
        "front_extend_product_list_form": [
            "wshop.front.apps.simple_search.forms.FilterProductListByQuery",
        ],
        "front_template_helper_namespace": [
            "wshop.front.apps.simple_search.template_helpers:TemplateHelpers"
        ]
    }


default_app_config = "wshop.front.apps.simple_search.SimpleSearchAppConfig"
