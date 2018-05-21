# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import pytest

from wshop.testing import factories
from wshop.utils.excs import Problem
from wshop.xtheme.editing import is_edit_mode
from wshop.xtheme.views.command import command_dispatch
from wshop_tests.utils.faux_users import SuperUser


def test_edit_can_be_set_via_view(rf):
    request = rf.get("/")
    request.user = SuperUser()
    request.shop = factories.get_default_shop()
    request.session = {}
    request.POST = {"command": "edit_on"}
    command_dispatch(request)
    assert is_edit_mode(request)
    request.POST = {"command": "edit_off"}
    command_dispatch(request)
    assert not is_edit_mode(request)


def test_dispatch_view_kvetches_at_unknown_commands(rf):
    with pytest.raises(Problem):
        command_dispatch(rf.post("/"))
