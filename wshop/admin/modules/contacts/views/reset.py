# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _

from wshop.admin.modules.users.views.password import UserResetPasswordView
from wshop.admin.utils.urls import get_model_url
from wshop.core.models import Contact
from wshop.utils.excs import Problem


class ContactResetPasswordView(UserResetPasswordView):
    def get_contact(self):
        contact = Contact.objects.get(pk=self.kwargs[self.pk_url_kwarg])
        limited = (settings.WSHOP_ENABLE_MULTIPLE_SHOPS and settings.WSHOP_MANAGE_CONTACTS_PER_SHOP and
                   not self.request.user.is_superuser)
        if limited:
            shop = self.request.shop
            if shop not in contact.shops.all():
                raise PermissionDenied()
        return contact

    def get_object(self, queryset=None):
        contact = self.get_contact()
        user = getattr(contact, "user", None)
        if not user:
            raise Problem(_(u"The contact does not have an associated user."))
        return user

    def get_success_url(self):
        return get_model_url(self.get_contact())
