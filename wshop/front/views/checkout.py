# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views.generic import View
from six.moves import urllib

from wshop.front.checkout import CheckoutProcess, VerticalCheckoutProcess
from wshop.utils.importing import cached_load

__all__ = ["BaseCheckoutView"]


class BaseCheckoutView(View):
    url_namespace = 'wshop:checkout'
    phase_specs = []
    empty_phase_spec = None
    initial_phase = None
    process_class = CheckoutProcess

    def dispatch(self, request, *args, **kwargs):
        if request.basket.is_empty and self.empty_phase_spec:
            self.phase_specs = [self.empty_phase_spec]
            phase_identifier = "empty"
        else:
            phase_identifier = kwargs.get("phase", self.initial_phase)

        process = self.process_class(
            phase_specs=self.phase_specs,
            phase_kwargs=dict(request=request, args=args, kwargs=kwargs),
            view=self)
        request.basket = process.basket
        if phase_identifier == "reset":
            process.reset()
            return redirect(self.get_url())

        current_phase = process.prepare_current_phase(phase_identifier)
        if not current_phase.final and current_phase.identifier != phase_identifier:
            url = current_phase.get_url()
            params = ("?" + urllib.parse.urlencode(request.GET)) if request.GET else ""
            return redirect(url + params)
        return current_phase.dispatch(request, *args, **kwargs)

    def get_url(self, **kwargs):
        """
        Get URL for given kwargs within the checkout process in this view.

        This can be overriden in a subclass to customize the URLs.

        :rtype: str
        """
        return reverse(self.url_namespace, kwargs=kwargs)

    def get_phase_url(self, phase):
        """
        Get URL for the given phase in the checkout process of this view.

        :type phase: wshop.front.checkout.CheckoutPhaseViewMixin
        :rtype: str
        """
        return self.get_url(phase=phase.identifier)


class DefaultCheckoutView(BaseCheckoutView):
    phase_specs = [
        "wshop.front.checkout.addresses:AddressesPhase",
        "wshop.front.checkout.methods:MethodsPhase",
        "wshop.front.checkout.methods:ShippingMethodPhase",
        "wshop.front.checkout.methods:PaymentMethodPhase",
        "wshop.front.checkout.confirm:ConfirmPhase",
    ]
    empty_phase_spec = "wshop.front.checkout.empty:EmptyPhase"


class SinglePageCheckoutView(DefaultCheckoutView):
    initial_phase = "addresses"
    process_class = VerticalCheckoutProcess


class CheckoutViewWithLoginAndRegister(BaseCheckoutView):
    phase_specs = [
        "wshop.front.checkout.checkout_method:CheckoutMethodPhase",
        "wshop.front.checkout.checkout_method:RegisterPhase",
        "wshop.front.checkout.addresses:AddressesPhase",
        "wshop.front.checkout.methods:MethodsPhase",
        "wshop.front.checkout.methods:ShippingMethodPhase",
        "wshop.front.checkout.methods:PaymentMethodPhase",
        "wshop.front.checkout.confirm:ConfirmPhase",
    ]
    empty_phase_spec = "wshop.front.checkout.empty:EmptyPhase"


def get_checkout_view():
    view = cached_load("WSHOP_CHECKOUT_VIEW_SPEC")
    if hasattr(view, "as_view"):  # pragma: no branch
        view = view.as_view()
    return view
