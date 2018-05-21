# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http.response import JsonResponse
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from wshop.admin.base import AdminModule, MenuEntry, Notification
from wshop.admin.menu import SETTINGS_MENU_CATEGORY
from wshop.admin.shop_provider import get_shop
from wshop.admin.utils.permissions import get_default_model_permissions
from wshop.admin.utils.urls import (
    admin_url, derive_model_url, get_edit_and_list_urls
)
from wshop.notify.enums import Priority
from wshop.notify.models import Notification as NotificationModel
from wshop.notify.models import Script

SCRIPT_TEMPLATES_PROVIDE_CATEGORY = 'notify_script_template'


class NotifyAdminModule(AdminModule):
    name = _(u"Notifications")
    breadcrumbs_menu_entry = MenuEntry(name, "wshop_admin:notify.script.list")

    def get_urls(self):
        permissions = get_default_model_permissions(NotificationModel)
        return [
            admin_url(
                "notify/script-item-editor/",
                "wshop.notify.admin_module.views.script_item_editor",
                name="notify.script-item-editor",
                permissions=permissions
            ),
            admin_url(
                "notify/script/content/(?P<pk>\d+)/",
                "wshop.notify.admin_module.views.EditScriptContentView",
                name="notify.script.edit-content",
                permissions=permissions
            ),
            admin_url(
                "notify/mark-read/(?P<pk>\d+)/$",
                self.mark_notification_read_view,
                name="notify.mark-read",
                permissions=permissions
            ),
            admin_url(
                "notify/script-template/",
                "wshop.notify.admin_module.views.ScriptTemplateView",
                name="notify.script-template",
                permissions=permissions
            ),
            admin_url(
                "notify/script-template-config/(?P<id>.+)/",
                "wshop.notify.admin_module.views.ScriptTemplateConfigView",
                name="notify.script-template-config",
                permissions=permissions
            ),
            admin_url(
                "notify/script-template-edit/(?P<pk>.+)/",
                "wshop.notify.admin_module.views.ScriptTemplateEditView",
                name="notify.script-template-edit",
                permissions=permissions
            ),
        ] + get_edit_and_list_urls(
            url_prefix="^notify/script",
            view_template="wshop.notify.admin_module.views.Script%sView",
            name_template="notify.script.%s",
            permissions=permissions
        )

    def get_menu_entries(self, request):
        return [
            MenuEntry(
                text=_("Notifications"), icon="fa fa-code",
                url="wshop_admin:notify.script.list",
                category=SETTINGS_MENU_CATEGORY,
                subcategory="other_settings",
                ordering=9,
                aliases=[_("Show notification scripts")]
            )
        ]

    def get_required_permissions(self):
        return get_default_model_permissions(NotificationModel)

    @csrf_exempt
    def mark_notification_read_view(self, request, pk):
        shop = get_shop(request)
        if request.method == "POST":
            try:
                notif = NotificationModel.objects.for_user(request.user).filter(shop=shop).get(pk=pk)
            except ObjectDoesNotExist:
                return JsonResponse({"error": "no such notification"})
            notif.mark_read(request.user)
            return JsonResponse({"ok": True})
        return JsonResponse({"error": "POST only"})

    def get_notifications(self, request):
        shop = get_shop(request)
        notif_qs = NotificationModel.objects.unread_for_user(request.user).filter(shop=shop).order_by("-id")[:15]

        for notif in notif_qs:
            if notif.priority == Priority.HIGH:
                kind = "warning"
            elif notif.priority == Priority.CRITICAL:
                kind = "danger"
            else:
                kind = "info"

            yield Notification(
                text=notif.message,
                url=notif.url,
                kind=kind,
                dismissal_url=reverse("wshop_admin:notify.mark-read", kwargs={"pk": notif.pk}),
                datetime=notif.created_on
            )

    def get_model_url(self, object, kind, shop=None):
        return derive_model_url(Script, "wshop_admin:notify.script", object, kind)
