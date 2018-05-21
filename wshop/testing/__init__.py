# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class WshopTestingAppConfig(AppConfig):
    name = "wshop.testing"
    verbose_name = "Wshop Testing & Demo Utilities"
    label = "wshop_testing"
    provides = {
        "admin_module": [
            "wshop.testing.admin_module:TestingAdminModule"
        ],
        "service_provider_admin_form": [
            "wshop.testing.service_forms:PseudoPaymentProcessorForm",
            "wshop.testing.service_forms:PaymentWithCheckoutPhaseForm",
            "wshop.testing.service_forms:CarrierWithCheckoutPhaseForm",
        ],
        "front_service_checkout_phase_provider": [
            "wshop.testing.simple_checkout_phase.PaymentPhaseProvider",
            "wshop.testing.simple_checkout_phase.ShipmentPhaseProvider",
        ],
        "admin_contact_toolbar_button": [
            "wshop.testing.admin_module.toolbar:MockContactToolbarButton",
        ],
        "admin_contact_toolbar_action_item": [
             "wshop.testing.admin_module.toolbar:MockContactToolbarActionItem",
        ],
        "admin_contact_edit_toolbar_button": [
            "wshop.testing.admin_module.toolbar:MockContactToolbarButton",
        ],
        "admin_product_toolbar_action_item": [
            "wshop.testing.admin_module.toolbar:MockProductToolbarActionItem",
        ],
        "admin_contact_section": [
            "wshop.testing.admin_module.sections:MockContactSection",
        ],
        "xtheme": [
            __name__ + ".themes:WshopTestingTheme",
            __name__ + ".themes:WshopTestingThemeWithCustomBase",
        ],
    }


default_app_config = "wshop.testing.WshopTestingAppConfig"
