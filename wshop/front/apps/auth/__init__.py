# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class AuthAppConfig(AppConfig):
    name = "wshop.front.apps.auth"
    verbose_name = "Wshop Frontend - User Authentication"
    label = "wshop_front.auth"

    provides = {
        "front_urls": [
            "wshop.front.apps.auth.urls:urlpatterns"
        ],
    }


default_app_config = "wshop.front.apps.auth.AuthAppConfig"
