# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from filer.fields.file import AdminFileWidget

from wshop.admin.forms.widgets import FileDnDUploaderWidget
from wshop.utils.multilanguage_model_form import MultiLanguageModelForm


class WshopAdminForm(MultiLanguageModelForm):

    def __init__(self, **kwargs):
        super(WshopAdminForm, self).__init__(**kwargs)
        for field in self.fields:
            if issubclass(self.fields[field].widget.__class__, AdminFileWidget):
                self.fields[field].widget = FileDnDUploaderWidget(
                    upload_path="/default", kind="images", clearable=True)
