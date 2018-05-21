# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

"""
Modify these only for Wshop tests. For testing modify urls.py instead.
"""
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('wshop.admin.urls', namespace="wshop_admin", app_name="wshop_admin")),
    url(r'^api/', include('wshop.api.urls')),
    url(r'^', include('wshop.front.urls', namespace="wshop", app_name="wshop")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
