# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django_jinja import library

from wshop.xtheme import parsing
from wshop.xtheme.template_ns import XthemeNamespace

# TODO: Use `library.extension()` when it's fixed in a release
# (when https://github.com/niwinz/django-jinja/commit/b7579ae1b5deff6afb937c3bb07b576b4cb4fe00 lands)
global_vars = library._local_env["globals"]
extensions = library._local_env["extensions"]

global_vars["xtheme"] = XthemeNamespace()
extensions.update(set(parsing.EXTENSIONS))
