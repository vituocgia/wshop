# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from wshop.apps.provides import override_provides
from wshop.front.templatetags.wshop_front import _get_helpers


class TestNs:
    name = "badgers"

    def snake(self):
        return True


def test_extendable_helper_ns():
    with override_provides("front_template_helper_namespace", [
        "%s:TestNs" % __name__
    ]):
        ns = _get_helpers()
        assert ns.badgers.snake()
