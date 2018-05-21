# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import unicode_literals

import warnings

import django.contrib.auth.views as auth_views
from django.conf.urls import url
from django.contrib.auth import logout as do_logout
from django.views.decorators.csrf import csrf_exempt
from django.views.i18n import set_language

from wshop.admin.forms import EmailAuthenticationForm
from wshop.admin.module_registry import get_module_urls
from wshop.admin.utils.urls import admin_url, AdminRegexURLPattern
from wshop.admin.views.dashboard import DashboardView
from wshop.admin.views.home import HomeView
from wshop.admin.views.menu import MenuView
from wshop.admin.views.search import SearchView
from wshop.admin.views.select import MultiselectAjaxView
from wshop.admin.views.tour import TourView
from wshop.admin.views.wizard import WizardView
from wshop.utils.i18n import javascript_catalog_all


def login(request, **kwargs):
    if not request.user.is_anonymous() and request.method == "POST":  # We're logging in, so log out first
        do_logout(request)
    kwargs.setdefault("extra_context", {})["error"] = request.GET.get("error")
    return auth_views.login(request, authentication_form=EmailAuthenticationForm, **kwargs)


def get_urls():
    urls = []
    urls.extend(get_module_urls())

    urls.extend([
        admin_url(r'^$', DashboardView.as_view(), name='dashboard'),
        admin_url(r'^home/$', HomeView.as_view(), name='home'),
        admin_url(r'^wizard/$', WizardView.as_view(), name='wizard'),
        admin_url(r'^tour/$', TourView.as_view(), name='tour'),
        admin_url(r'^search/$', SearchView.as_view(), name='search'),
        admin_url(r'^select/$', MultiselectAjaxView.as_view(), name='select'),
        admin_url(r'^menu/$', MenuView.as_view(), name='menu'),
        admin_url(
            r'^login/$',
            login,
            kwargs={"template_name": "wshop/admin/auth/login.jinja"},
            name='login',
            require_authentication=False
        ),
        admin_url(
            r'^logout/$',
            auth_views.logout,
            kwargs={"template_name": "wshop/admin/auth/logout.jinja"},
            name='logout',
            require_authentication=False
        ),
        admin_url(
            r'^set-language/$',
            csrf_exempt(set_language),
            name="set-language"
        ),
    ])

    for u in urls:  # pragma: no cover
        if not isinstance(u, AdminRegexURLPattern):
            warnings.warn("Admin URL %r is not an AdminRegexURLPattern" % u)

    # Add Django javascript catalog url
    urls.append(url(r'^i18n.js$', javascript_catalog_all, name='js-catalog'))

    return tuple(urls)


urlpatterns = get_urls()
