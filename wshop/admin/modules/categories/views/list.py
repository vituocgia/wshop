# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from wshop.admin.utils.picotable import ChoicesFilter, Column, MPTTFilter
from wshop.admin.utils.views import PicotableListView
from wshop.core.models import Category, CategoryStatus, CategoryVisibility


class CategoryListView(PicotableListView):
    model = Category
    default_columns = [
        Column("image", _("Image"), sortable=False, linked=True, raw=True),
        Column(
            "name", _(u"Name"), sortable=False, display="format_name", linked=True,
            filter_config=MPTTFilter(
                choices="get_name_filter_choices",
                filter_field="id"
            )
        ),
        Column(
            "status", _(u"Status"),
            filter_config=ChoicesFilter(
                choices=CategoryStatus.choices,
                default=CategoryStatus.VISIBLE.value
            )
        ),
        Column("visibility", _(u"Visibility"), filter_config=ChoicesFilter(choices=CategoryVisibility.choices)),
    ]

    def get_name_filter_choices(self):
        choices = []
        shop = self.request.shop
        for c in Category.objects.all_except_deleted(shop=shop):
            name = self.format_name(c)
            choices.append((c.pk, name))
        return choices

    def get_queryset(self):
        return Category.objects.all_except_deleted(shop=self.request.shop)

    def format_name(self, instance, *args, **kwargs):
        level = getattr(instance, instance._mptt_meta.level_attr)
        return ('---' * level) + ' ' + instance.name

    def get_object_abstract(self, instance, item):
        return [
            {"text": "%s" % instance, "class": "header"},
            {"title": _(u"Status"), "text": item.get("status")},
        ]
