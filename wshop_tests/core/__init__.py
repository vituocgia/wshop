# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class AppConfig(AppConfig):
    name = 'wshop_tests.core'
    label = 'wshop_tests_core'

    provides = {
        "module_test_module": [
            "wshop_tests.core.module_test_module:ModuleTestModule",
            "wshop_tests.core.module_test_module:AnotherModuleTestModule",
        ]
    }


default_app_config = 'wshop_tests.core.AppConfig'
