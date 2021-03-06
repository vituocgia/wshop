# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest
from django.test import override_settings

from wshop.admin.modules.shops.views.edit import ShopEditView
from wshop.testing.factories import get_default_shop
from wshop.testing.utils import apply_request_middleware
from wshop.utils.excs import Problem


@pytest.mark.django_db
def test_multishop_edit_view(rf, admin_user):
    get_default_shop()

    request = apply_request_middleware(rf.get("/"), user=admin_user)
    view = ShopEditView(request=request, kwargs={"pk": None})

    with override_settings(WSHOP_ENABLE_MULTIPLE_SHOPS=False):
        with pytest.raises(Problem):
            view.get_object()  # Now view object should throw Problem

    with override_settings(WSHOP_ENABLE_MULTIPLE_SHOPS=True):
        new_shop = view.get_object()
        assert new_shop.pk is None
