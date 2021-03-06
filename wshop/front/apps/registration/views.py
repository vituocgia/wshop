# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.utils.http import is_safe_url
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View
from registration.backends.default import views as default_views
from registration.backends.simple import views as simple_views

from wshop import configuration
from wshop.core.models import get_company_contact, get_person_contact
from wshop.front.apps.registration.forms import CompanyRegistrationForm
from wshop.front.template_helpers import urls


def activation_complete(request):
    messages.success(request, _("Activation successful!"))
    if urls.has_url('wshop:customer_edit'):
        return redirect('wshop:customer_edit')
    else:
        return redirect(settings.LOGIN_REDIRECT_URL)


def registration_complete(request):
    if settings.WSHOP_REGISTRATION_REQUIRES_ACTIVATION:
        messages.success(
            request, _("Registration complete. Please follow the instructions sent to your email address."))
    return redirect(settings.LOGIN_REDIRECT_URL)


class RegistrationViewMixin(object):
    template_name = "wshop/registration/register.jinja"

    def get_success_url(self, *args, **kwargs):
        url = self.request.POST.get(REDIRECT_FIELD_NAME)
        if url and is_safe_url(url, self.request.get_host()):
            return url
        return ('wshop:registration_complete', (), {})

    def register(self, form):
        user = super(RegistrationViewMixin, self).register(form)

        if settings.WSHOP_ENABLE_MULTIPLE_SHOPS and settings.WSHOP_MANAGE_CONTACTS_PER_SHOP:
            get_person_contact(user).shops.add(self.request.shop)

        return user


class RegistrationNoActivationView(RegistrationViewMixin, simple_views.RegistrationView):
    pass


class RegistrationWithActivationView(RegistrationViewMixin, default_views.RegistrationView):
    SEND_ACTIVATION_EMAIL = False


class RegistrationView(View):
    def dispatch(self, request, *args, **kwargs):
        if settings.WSHOP_REGISTRATION_REQUIRES_ACTIVATION:
            view_class = RegistrationWithActivationView
        else:
            view_class = RegistrationNoActivationView

        return view_class.as_view()(request, *args, **kwargs)


class CompanyRegistrationView(RegistrationViewMixin, default_views.RegistrationView):
    template_name = "wshop/registration/company_register.jinja"
    form_class = CompanyRegistrationForm

    SEND_ACTIVATION_EMAIL = False

    def dispatch(self, request, *args, **kwargs):
        if not configuration.get(None, "allow_company_registration"):
            return HttpResponseNotFound()
        return super(CompanyRegistrationView, self).dispatch(request, *args, **kwargs)

    def register(self, form):
        user = super(CompanyRegistrationView, self).register(form)

        if settings.WSHOP_ENABLE_MULTIPLE_SHOPS and settings.WSHOP_MANAGE_CONTACTS_PER_SHOP:
            company = get_company_contact(user)
            company.shops.add(self.request.shop)


class ActivationView(default_views.ActivationView):
    template_name = "wshop/registration/activation_failed.jinja"

    def get_success_url(self, *args, **kwargs):
        return ('wshop:registration_activation_complete', (), {})
