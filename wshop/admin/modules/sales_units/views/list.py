# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from wshop.admin.utils.picotable import Column, TextFilter
from wshop.admin.utils.views import PicotableListView
from wshop.core.models import DisplayUnit, SalesUnit


class UnitListView(PicotableListView):
    default_columns = [
        Column("name", _(u"Name"), sort_field="translations__name", display="name", filter_config=TextFilter(
            filter_field="translations__name",
            placeholder=_("Filter by name...")
        )),
        Column("symbol", _(u"Symbol"), sort_field="translations__symbol", display="symbol"),
        Column("decimals", _(u"Allowed decimals")),
    ]

    def get_queryset(self):
        return self.model.objects.all()


class SalesUnitListView(UnitListView):
    model = SalesUnit


class DisplayUnitListView(UnitListView):
    model = DisplayUnit
