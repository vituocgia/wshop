# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse_lazy

from wshop.admin.form_part import FormPartsViewMixin, SaveFormPartsMixin
from wshop.admin.modules.categories.form_parts import (
    CategoryBaseFormPart, CategoryProductFormPart
)
from wshop.admin.toolbar import get_default_edit_toolbar
from wshop.admin.utils.tour import is_tour_complete
from wshop.admin.utils.views import CreateOrUpdateView
from wshop.core.models import Category


class CategoryEditView(SaveFormPartsMixin, FormPartsViewMixin, CreateOrUpdateView):
    model = Category
    template_name = "wshop/admin/categories/edit.jinja"
    context_object_name = "category"
    base_form_part_classes = [CategoryBaseFormPart, CategoryProductFormPart]
    form_part_class_provide_key = "admin_category_form_part"

    def get_toolbar(self):
        save_form_id = self.get_save_form_id()
        object = self.get_object()
        delete_url = reverse_lazy("wshop_admin:category.delete", kwargs={"pk": object.pk}) if object.pk else None
        return get_default_edit_toolbar(self, save_form_id, delete_url=delete_url)

    def get_context_data(self, **kwargs):
        context = super(CategoryEditView, self).get_context_data(**kwargs)
        context["tour_key"] = "category"
        context["tour_complete"] = is_tour_complete("category")
        return context

    def form_valid(self, form):
        return self.save_form_parts(form)

    def get_queryset(self):
        return Category.objects.all_except_deleted(shop=self.request.shop)
