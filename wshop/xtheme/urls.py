# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf.urls import url

from wshop.xtheme.views.command import command_dispatch
from wshop.xtheme.views.editor import EditorView
from wshop.xtheme.views.extra import extra_view_dispatch

urlpatterns = [
    url(r"^xtheme/editor/$", EditorView.as_view(), name="xtheme_editor"),
    url(r"^xtheme/(?P<view>.+)/*$", extra_view_dispatch, name="xtheme_extra_view"),
    url(r"^xtheme/$", command_dispatch, name="xtheme"),
]
