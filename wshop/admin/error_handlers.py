# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.conf import settings
from django.shortcuts import render

from wshop.core.error_handling import ErrorPageHandler


class AdminPageErrorHandler(ErrorPageHandler):
    """
    Page Error handler for Wshop Admin
    """

    @classmethod
    def can_handle_error(cls, request, error_status):
        # we can't handle 404 errors, neither static or media files
        # since 404 errors means no URL match,
        # how can we figure out, in a elegant way if we are in the Admin?
        if (error_status == 404 or request.path.startswith(settings.STATIC_URL) or
                request.path.startswith(settings.MEDIA_URL)):
            return False

        # we are in a view which belongs to the Admin
        elif request.resolver_match:
            from wshop.admin import WshopAdminAppConfig
            return (request.resolver_match.app_name == WshopAdminAppConfig.label)

        return False

    @classmethod
    def handle_error(cls, request, error_status):
        return render(request, "wshop/admin/errors/{}.jinja".format(error_status), status=error_status)
