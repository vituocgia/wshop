# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import wshop.apps


class AppConfig(wshop.apps.AppConfig):
    name = __name__
    verbose_name = _("Simple CMS")
    label = "wshop_simple_cms"

    provides = {
        "front_urls_post": [__name__ + ".urls:urlpatterns"],
        "admin_module": [
            "wshop.simple_cms.admin_module:SimpleCMSAdminModule"
        ],
        "front_template_helper_namespace": [
            "wshop.simple_cms.template_helpers:SimpleCMSTemplateHelpers"
        ],
        "xtheme_plugin": [
            "wshop.simple_cms.plugins:PageLinksPlugin"
        ],
    }


default_app_config = __name__ + ".AppConfig"
