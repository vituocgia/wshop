# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from wshop.api.admin_module.forms import APIPermissionForm


class APIPermissionView(FormView):
    template_name = "wshop/api/admin/permissions.jinja"
    form_class = APIPermissionForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, _("API permissions saved"))
        return redirect("wshop_admin:api_permission")
