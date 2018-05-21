# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps import AppConfig


class CampaignAppConfig(AppConfig):
    name = "wshop.campaigns"
    verbose_name = "Wshop Campaigns"
    label = "campaigns"
    provides = {
        "admin_contact_group_form_part": [
            "wshop.campaigns.admin_module.form_parts:SalesRangesFormPart"
        ],
        "discount_module": [
            "wshop.campaigns.modules:CatalogCampaignModule"
        ],
        "order_source_modifier_module": [
            "wshop.campaigns.modules:BasketCampaignModule"
        ],
        "admin_module": [
            "wshop.campaigns.admin_module:CampaignAdminModule",
        ],
        "admin_product_section": [
            "wshop.campaigns.admin_module.sections:ProductCampaignsSection"
        ],
        "campaign_basket_condition": [
            "wshop.campaigns.admin_module.forms:BasketTotalProductAmountConditionForm",
            "wshop.campaigns.admin_module.forms:BasketTotalAmountConditionForm",
            "wshop.campaigns.admin_module.forms:BasketTotalUndiscountedProductAmountConditionForm",
            "wshop.campaigns.admin_module.forms:BasketMaxTotalProductAmountConditionForm",
            "wshop.campaigns.admin_module.forms:BasketMaxTotalAmountConditionForm",
            "wshop.campaigns.admin_module.forms:ProductsInBasketConditionForm",
            "wshop.campaigns.admin_module.forms:ContactGroupBasketConditionForm",
            "wshop.campaigns.admin_module.forms:ContactBasketConditionForm",
            "wshop.campaigns.admin_module.forms:CategoryProductsBasketConditionForm",
            "wshop.campaigns.admin_module.forms:HourBasketConditionForm",
        ],
        "campaign_basket_discount_effect_form": [
            "wshop.campaigns.admin_module.forms:BasketDiscountAmountForm",
            "wshop.campaigns.admin_module.forms:BasketDiscountPercentageForm",
            "wshop.campaigns.admin_module.forms:DiscountPercentageFromUndiscountedForm",
        ],
        "campaign_basket_line_effect_form": [
            "wshop.campaigns.admin_module.forms:FreeProductLineForm",
            "wshop.campaigns.admin_module.forms:DiscountFromProductForm",
            "wshop.campaigns.admin_module.forms:DiscountFromCategoryProductsForm",
        ],
        "campaign_context_condition": [
            "wshop.campaigns.admin_module.forms:ContactGroupConditionForm",
            "wshop.campaigns.admin_module.forms:ContactConditionForm",
            "wshop.campaigns.admin_module.forms:HourConditionForm",
        ],
        "campaign_catalog_filter": [
            "wshop.campaigns.admin_module.forms:ProductTypeFilterForm",
            "wshop.campaigns.admin_module.forms:ProductFilterForm",
            "wshop.campaigns.admin_module.forms:CategoryFilterForm"
        ],
        "campaign_product_discount_effect_form": [
            "wshop.campaigns.admin_module.forms:ProductDiscountAmountForm",
            "wshop.campaigns.admin_module.forms:ProductDiscountPercentageForm",
        ],
        "reports": [
            "wshop.campaigns.reports:CouponsUsageReport"
        ]
    }

    def ready(self):
        from django.db.models.signals import m2m_changed, post_save
        from wshop.campaigns.models import CategoryFilter, ProductFilter, ProductTypeFilter
        from wshop.campaigns.models import ContactCondition, ContactGroupCondition
        from wshop.campaigns.signal_handlers import (
            invalidate_context_condition_cache,
            update_customers_groups, update_filter_cache
        )
        from wshop.core.models import ContactGroup, Payment, ShopProduct
        post_save.connect(
            update_customers_groups,
            sender=Payment,
            dispatch_uid="contact_group_sales:update_customers_groups"
        )

        # Invalidate context condition caches
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactGroup.members.through,
            dispatch_uid="campaigns:invalidate_caches_for_contact_group_m2m_change"
        )
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactCondition.contacts.through,
            dispatch_uid="campaigns:invalidate_caches_for_contacts_condition_m2m_change"
        )
        m2m_changed.connect(
            invalidate_context_condition_cache,
            sender=ContactGroupCondition.contact_groups.through,
            dispatch_uid="campaigns:invalidate_caches_for_contact_group_condition_m2m_change"
        )

        # Invalidate context filter caches
        m2m_changed.connect(
            update_filter_cache,
            sender=CategoryFilter.categories.through,
            dispatch_uid="campaigns:invalidate_caches_for_category_filter_m2m_change"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ProductFilter.products.through,
            dispatch_uid="campaigns:invalidate_caches_for_product_filter_m2m_change"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ProductTypeFilter.product_types.through,
            dispatch_uid="campaigns:invalidate_caches_for_product_type_filter_m2m_change"
        )
        post_save.connect(
            update_filter_cache,
            sender=ShopProduct,
            dispatch_uid="campaigns:invalidate_caches_for_shop_product_save"
        )
        m2m_changed.connect(
            update_filter_cache,
            sender=ShopProduct.categories.through,
            dispatch_uid="campaigns:invalidate_caches_for_shop_product_m2m_change"
        )
