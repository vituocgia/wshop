# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import requests
from django.utils.translation import ugettext_lazy as _

from wshop.admin.base import AdminModule
from wshop.admin.dashboard import DashboardContentBlock
from wshop.core import cache

SECONDS_IN_DAY = 86400


class WshopSupportModule(AdminModule):
    name = _("Wshop Support")

    def _get_resource(self, request, resource_id):
        cache_key = "WSHOPCOM_API_%s_%s" % (request.LANGUAGE_CODE, resource_id)
        resource = cache.get(cache_key)
        if not resource:
            try:
                r = requests.get("https://www.wshop.com/%s/api/%s/" % (request.LANGUAGE_CODE, resource_id))
                resource = r.json()
                cache.set(cache_key, resource, timeout=SECONDS_IN_DAY)
            except Exception:
                pass
        return resource or {}

    def _get_article_block(self, request):
        articles = self._get_resource(request, "articles")
        if articles.get("articles"):
            article_block = DashboardContentBlock.by_rendering_template(
                "articles", request, "wshop/admin/support/_articles_dashboard_block.jinja", articles)
            article_block.size = "small"
            return [article_block]
        return []

    def _get_support_block(self, request):
        support_block = DashboardContentBlock.by_rendering_template(
            "support", request, "wshop/admin/support/_support_dashboard_block.jinja", {})
        support_block.size = "small"
        return [support_block]

    def get_dashboard_blocks(self, request):
        blocks = []
        blocks.extend(self._get_article_block(request))
        blocks.extend(self._get_support_block(request))
        return blocks
