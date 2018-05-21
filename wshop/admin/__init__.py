# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig
from wshop.apps.settings import validate_templates_configuration


class WshopAdminAppConfig(AppConfig):
    name = "wshop.admin"
    verbose_name = "Wshop Admin"
    label = "wshop_admin"
    required_installed_apps = ["bootstrap3"]
    provides = {
        "admin_module": [
            "wshop.admin.modules.system:SystemModule",
            "wshop.admin.modules.products:ProductModule",
            "wshop.admin.modules.product_types:ProductTypeModule",
            "wshop.admin.modules.media:MediaModule",
            "wshop.admin.modules.orders:OrderModule",
            "wshop.admin.modules.taxes:TaxModule",
            "wshop.admin.modules.categories:CategoryModule",
            "wshop.admin.modules.contacts:ContactModule",
            "wshop.admin.modules.contact_groups:ContactGroupModule",
            "wshop.admin.modules.currencies:CurrencyModule",
            "wshop.admin.modules.customers_dashboard:CustomersDashboardModule",
            "wshop.admin.modules.permission_groups:PermissionGroupModule",
            "wshop.admin.modules.users:UserModule",
            "wshop.admin.modules.service_providers:ServiceProviderModule",
            "wshop.admin.modules.services:PaymentMethodModule",
            "wshop.admin.modules.services:ShippingMethodModule",
            "wshop.admin.modules.attributes:AttributeModule",
            "wshop.admin.modules.sales_units:DisplayUnitModule",
            "wshop.admin.modules.sales_units:SalesUnitModule",
            "wshop.admin.modules.sales_dashboard:SalesDashboardModule",
            "wshop.admin.modules.shops:ShopModule",
            "wshop.admin.modules.demo:DemoModule",
            "wshop.admin.modules.manufacturers:ManufacturerModule",
            "wshop.admin.modules.suppliers:SupplierModule",
            "wshop.admin.modules.support:WshopSupportModule",
            "wshop.admin.modules.sample_data:SampleDataAdminModule",
            "wshop.admin.modules.settings.SettingsModule"
        ],
        "admin_shop_form_part": [
            "wshop.admin.modules.settings.form_parts.OrderConfigurationFormPart"
        ],
        "service_provider_admin_form": [
            "wshop.admin.modules.service_providers.forms:CustomCarrierForm",
            "wshop.admin.modules.service_providers.forms:CustomPaymentProcessorForm"
        ],
        "carrier_wizard_form_def": [
            "wshop.admin.modules.service_providers.wizard_form_defs:ManualShippingWizardFormDef"
        ],
        "payment_processor_wizard_form_def": [
            "wshop.admin.modules.service_providers.wizard_form_defs:ManualPaymentWizardFormDef"
        ],
        "service_behavior_component_form": [
            "wshop.admin.modules.services.forms:FixedCostBehaviorComponentForm",
            "wshop.admin.modules.services.forms:WaivingCostBehaviorComponentForm",
            "wshop.admin.modules.services.forms:WeightLimitsBehaviorComponentForm",
            "wshop.admin.modules.services.forms:GroupAvailabilityBehaviorComponentForm",
            "wshop.admin.modules.services.forms.StaffOnlyBehaviorComponentForm",
            "wshop.admin.modules.services.forms.OrderTotalLimitBehaviorComponentForm",
            "wshop.admin.modules.services.forms.CountryLimitBehaviorComponentForm",
        ],
        "service_behavior_component_form_part": [
            "wshop.admin.modules.services.weight_based_pricing.WeightBasedPricingFormPart"
        ],
        "admin_order_section": [
            "wshop.admin.modules.orders.sections:PaymentOrderSection",
            "wshop.admin.modules.orders.sections:LogEntriesOrderSection",
            "wshop.admin.modules.orders.sections:ShipmentSection",
            "wshop.admin.modules.orders.sections:AdminCommentSection",
        ],
        "admin_contact_section": [
            "wshop.admin.modules.contacts.sections:BasicInfoContactSection",
            "wshop.admin.modules.contacts.sections:AddressesContactSection",
            "wshop.admin.modules.contacts.sections:OrdersContactSection",
            "wshop.admin.modules.contacts.sections:MembersContactSection",
        ],
        "admin_product_section": [
            "wshop.admin.modules.products.sections:ProductOrdersSection"
        ],
        "admin_order_toolbar_action_item": [
            "wshop.admin.modules.orders.toolbar:CreatePaymentAction",
            "wshop.admin.modules.orders.toolbar:SetPaidAction",
            "wshop.admin.modules.orders.toolbar:CreateShipmentAction",
            "wshop.admin.modules.orders.toolbar:CreateRefundAction",
            "wshop.admin.modules.orders.toolbar:EditAddresses",
        ]
    }

    def ready(self):
        from wshop.core.order_creator.signals import order_creator_finished
        from wshop.admin.modules.orders.receivers import handle_custom_payment_return_requests

        order_creator_finished.connect(handle_custom_payment_return_requests,
                                       dispatch_uid='wshop.admin.handle_cash_payments')

        validate_templates_configuration()


default_app_config = "wshop.admin.WshopAdminAppConfig"
