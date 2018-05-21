# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
"""
WSGI config for wshop_workbench project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application  # noqa (E402)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wshop_workbench.settings")  # noqa

application = get_wsgi_application()
