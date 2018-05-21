# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.admin.forms.fields import WeekdayField
from wshop.admin.forms.widgets import TimeInput
from wshop.campaigns.models.context_conditions import (
    ContactCondition, ContactGroupCondition, HourCondition
)

from ._base import BaseRuleModelForm


class ContactGroupConditionForm(BaseRuleModelForm):
    class Meta(BaseRuleModelForm.Meta):
        model = ContactGroupCondition


class ContactConditionForm(BaseRuleModelForm):
    class Meta(BaseRuleModelForm.Meta):
        model = ContactCondition


class HourConditionForm(BaseRuleModelForm):
    days = WeekdayField()

    class Meta(BaseRuleModelForm.Meta):
        model = HourCondition
        widgets = {
            "hour_start": TimeInput(),
            "hour_end": TimeInput(),
        }

    def __init__(self, **kwargs):
        super(HourConditionForm, self).__init__(**kwargs)

        if self.instance:
            self.fields["days"].initial = self.instance.days.split(",")
