# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from wshop import configuration
from wshop.core.models import CompanyContact, PersonContact
from wshop.utils.form_group import FormGroup
from wshop.utils.importing import cached_load


class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyContact
        fields = ['name', 'name_ext', 'tax_number', 'email', 'phone', 'www']
        help_texts = {
            'name': _("Name of the company"),
            'email': None, 'phone': None,
        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['tax_number'].required = True
        address_form = cached_load('WSHOP_ADDRESS_MODEL_FORM')()
        for field in self.fields:
            if field not in ('name', 'tax_number', 'www'):
                address_formfield = address_form.fields.get(field)
                if address_formfield:
                    self.fields[field].required = address_formfield.required
                else:
                    del self.fields[field]


class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = PersonContact
        fields = ['first_name', 'last_name', 'email', 'phone']

    def __init__(self, **kwargs):
        super(ContactPersonForm, self).__init__(**kwargs)
        for (field_name, formfield) in self.fields.items():
            if field_name in ['first_name', 'last_name', 'email']:
                formfield.required = True
                formfield.help_text = None


class CompanyRegistrationForm(FormGroup):
    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        address_form_cls = cached_load('WSHOP_ADDRESS_MODEL_FORM')
        self.add_form_def('company', CompanyForm)
        self.add_form_def('billing', address_form_cls)
        self.add_form_def('contact_person', ContactPersonForm)
        self.add_form_def('user_account', UserCreationForm)

    def instantiate_forms(self):
        super(CompanyRegistrationForm, self).instantiate_forms()
        company_form = self.forms['company']
        billing_form = self.forms['billing']
        for field in list(billing_form.fields):
            billing_form.fields[field].help_text = None
            if field in company_form.fields:
                del billing_form.fields[field]

    def save(self, commit=True):
        company = self.forms['company'].save(commit=False)
        billing_address = self.forms['billing'].save(commit=False)
        person = self.forms['contact_person'].save(commit=False)
        user = self.forms['user_account'].save(commit=False)

        company.default_billing_address = billing_address
        company.default_shipping_address = billing_address

        for field in ['name', 'name_ext', 'email', 'phone']:
            setattr(billing_address, field, getattr(company, field))

        person.user = user

        user.first_name = person.first_name
        user.last_name = person.last_name
        user.email = person.email

        # If company registration requires approval,
        # company and person contacts will be created as inactive
        if configuration.get(None, "company_registration_requires_approval"):
            company.is_active = False
            person.is_active = False

        if commit:
            user.save()
            person.user = user
            person.save()
            billing_address.save()
            company.default_billing_address = billing_address
            company.default_shipping_address = billing_address
            company.save()
            company.members.add(person)

        return user