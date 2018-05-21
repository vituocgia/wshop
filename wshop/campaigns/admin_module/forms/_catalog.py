# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.campaigns.models.campaigns import CatalogCampaign

from ._base import BaseCampaignForm


class CatalogCampaignForm(BaseCampaignForm):
    class Meta(BaseCampaignForm.Meta):
        model = CatalogCampaign
        exclude = BaseCampaignForm.Meta.exclude + ["filters", "coupon"]
