# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig

from .manager import add_enabled_addons

__all__ = ["add_enabled_addons"]


class WshopAddonsAppConfig(AppConfig):
    name = "wshop.addons"
    verbose_name = "Wshop Addons"
    label = "wshop_addons"

    provides = {
        "admin_module": [
            "wshop.addons.admin_module:AddonModule",
        ]
    }


default_app_config = "wshop.addons.WshopAddonsAppConfig"
