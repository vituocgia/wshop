# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import six
from django import forms
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from enumfields import EnumIntegerField

from wshop.admin.forms.widgets import (
    QuickAddCategoryMultiSelect, QuickAddCategorySelect
)
from wshop.admin.utils.views import MassEditMixin
from wshop.core.models import (
    Category, Product, ShopProduct, ShopProductVisibility
)


class MassEditForm(forms.Form):
    name = forms.CharField(max_length=255, required=False)
    default_price_value = forms.DecimalField(label="Default Price", required=False)
    visibility = EnumIntegerField(ShopProductVisibility).formfield(label=_("Visibility"), required=False)
    primary_category = forms.ModelChoiceField(
        label=_("Primary Category"), queryset=Category.objects.all_except_deleted(), required=False,
        widget=QuickAddCategorySelect())
    categories = forms.ModelMultipleChoiceField(
        label=_("Additional Categories"), queryset=Category.objects.all_except_deleted(), required=False,
        widget=QuickAddCategoryMultiSelect())
    purchasable = forms.BooleanField(label=_("Purchasable"), required=False)


class ProductMassEditView(MassEditMixin, FormView):
    title = _("Mass Edit: Products")
    form_class = MassEditForm

    def form_valid(self, form):

        product_ids = ShopProduct.objects.filter(id__in=self.ids).values_list("product__id", flat=True)

        query = Q(id__in=product_ids)
        if isinstance(self.ids, six.string_types) and self.ids == "all":
            query = Q()
        for product in Product.objects.filter(query):
            shop_product = product.get_shop_instance(self.request.shop)

            for k, v in six.iteritems(form.cleaned_data):
                if not v:
                    continue
                if hasattr(product, k):
                    setattr(product, k, v)
                if hasattr(shop_product, k):
                    setattr(shop_product, k, v)
            product.save()
            shop_product.save()

        messages.success(self.request, _("Products changed successfully"))
        self.request.session["mass_action_ids"] = []
        return HttpResponseRedirect(reverse("wshop_admin:shop_product.list"))
