# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumField

from wshop.core.models import Shop
from wshop.importer.utils import get_importer_choices
from wshop.importer.utils.importer import ImportMode


class ImportSettingsForm(forms.Form):
    import_mode = EnumField(ImportMode).formfield(initial=ImportMode.CREATE_UPDATE, label=_("Import mode"))


class ImportForm(forms.Form):
    language = forms.ChoiceField(label=_("Importing language"), choices=settings.LANGUAGES, help_text=_(
        "The language of the data you would like to import."
    ))
    shop = forms.ChoiceField(label=_("Shop"), help_text=_("Select a shop you want import into"))
    importer = forms.ChoiceField(label=_("Importer"), help_text=_(
        "Select a importer type matching the data you would like to import"))
    file = forms.FileField(label=_("File"))

    def __init__(self, **kwargs):
        super(ImportForm, self).__init__(**kwargs)
        self.fields["shop"].choices = [(shop.pk, shop.name) for shop in Shop.objects.all()]
        self.fields["importer"].choices = get_importer_choices()
