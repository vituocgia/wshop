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


class FrontPageErrorHandler(ErrorPageHandler):
    """
    Page Error handler for Wshop Front
    """

    @classmethod
    def can_handle_error(cls, request, error_status):
        # we can't handle static or media files
        if (request.path.startswith(settings.STATIC_URL) or
                request.path.startswith(settings.MEDIA_URL)):
            return False

        # Front will handle everything else, for now
        return True

    @classmethod
    def handle_error(cls, request, error_status):
        return render(request, "wshop/front/errors/{}.jinja".format(error_status), status=error_status)
