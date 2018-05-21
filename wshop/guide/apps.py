# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import wshop.apps


class AppConfig(wshop.apps.AppConfig):
    name = "wshop.guide"
    verbose_name = "Wshop Guide"
    provides = {
        "admin_module": [
            "wshop.guide.admin_module:GuideAdminModule"
        ],
    }
