# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView

import wshop
from wshop.admin.dashboard import get_activity
from wshop.admin.module_registry import get_modules
from wshop.admin.utils.permissions import get_missing_permissions
from wshop.admin.utils.tour import is_tour_complete
from wshop.admin.utils.wizard import setup_wizard_complete
from wshop.core.telemetry import try_send_telemetry


class DashboardView(TemplateView):
    template_name = "wshop/admin/dashboard/dashboard.jinja"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context["version"] = wshop.__version__
        context["notifications"] = notifications = []
        context["blocks"] = blocks = []
        for module in get_modules():
            if not get_missing_permissions(self.request.user, module.get_required_permissions()):
                notifications.extend(module.get_notifications(request=self.request))
                blocks.extend(module.get_dashboard_blocks(request=self.request))
        context["activity"] = get_activity(request=self.request)
        context["tour_key"] = "dashboard"
        context["tour_complete"] = is_tour_complete("dashboard")
        return context

    def get(self, request, *args, **kwargs):
        try_send_telemetry(request)
        if not setup_wizard_complete(request):
            return HttpResponseRedirect(reverse("wshop_admin:wizard"))
        elif request.shop.maintenance_mode:
            return HttpResponseRedirect(reverse("wshop_admin:home"))
        return super(DashboardView, self).get(request, *args, **kwargs)
