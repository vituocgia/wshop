# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.

from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db.transaction import atomic

from wshop.admin.form_part import FormPartsViewMixin, SaveFormPartsMixin
from wshop.admin.toolbar import get_default_edit_toolbar
from wshop.admin.utils.views import CreateOrUpdateView
from wshop.core.models import ContactGroup

from .forms import ContactGroupBaseFormPart, ContactGroupMembersFormPart


class ContactGroupEditView(SaveFormPartsMixin, FormPartsViewMixin, CreateOrUpdateView):
    model = ContactGroup
    template_name = "wshop/admin/contact_groups/edit.jinja"
    context_object_name = "contact_group"
    base_form_part_classes = [ContactGroupBaseFormPart, ContactGroupMembersFormPart]
    form_part_class_provide_key = "admin_contact_group_form_part"

    @atomic
    def form_valid(self, form):
        return self.save_form_parts(form)

    def get_toolbar(self):
        save_form_id = self.get_save_form_id()
        object = self.get_object()
        delete_url = reverse_lazy("wshop_admin:contact_group.delete", kwargs={"pk": object.pk})
        return get_default_edit_toolbar(self, save_form_id, delete_url=delete_url if object.can_delete() else None)
