# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from wshop.front.views.checkout import SinglePageCheckoutView


class SinglePageCheckoutViewWithLoginAndRegister(SinglePageCheckoutView):
    initial_phase = "checkout_method"
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


urlpatterns = [
    url(r'^checkout/$', SinglePageCheckoutViewWithLoginAndRegister.as_view(), name='checkout'),
    url(r'^checkout/(?P<phase>.+)/$', SinglePageCheckoutViewWithLoginAndRegister.as_view(), name='checkout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sa/', include('wshop.admin.urls', namespace="wshop_admin", app_name="wshop_admin")),
    url(r'^api/', include('wshop.api.urls')),
    url(r'^', include('wshop.front.urls', namespace="wshop", app_name="wshop")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
