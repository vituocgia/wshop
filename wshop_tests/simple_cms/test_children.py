# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import datetime

import pytest

from wshop.simple_cms.views import PageView
from wshop.testing.factories import get_default_shop
from wshop.testing.utils import apply_request_middleware
from wshop_tests.simple_cms.utils import create_page


def check_children_content(request, page, children_content, children_visibility):
    view_func = PageView.as_view()
    response = view_func(request, url=page.url)
    response.render()

    assert page.get_html() in response.rendered_content
    assert bool(children_content in response.rendered_content) == children_visibility


@pytest.mark.django_db
def test_visible_children(rf):
    shop = get_default_shop()
    request = apply_request_middleware(rf.get("/"))
    assert request.user.is_anonymous()

    parent_content = "Parent content"
    page = create_page(available_from=datetime.date(1988, 1, 1), content=parent_content, shop=shop)
    children_content = "Children content"
    # Visible child
    create_page(available_from=datetime.date(2000, 1, 1), content=children_content, parent=page, shop=shop)

    assert page.list_children_on_page == False
    check_children_content(request, page, children_content, False)

    page.list_children_on_page = True
    page.save()
    check_children_content(request, page, children_content, True)


@pytest.mark.django_db
def test_invisible_children(rf):
    shop = get_default_shop()
    request = apply_request_middleware(rf.get("/"))

    parent_content = "Parent content"
    page = create_page(available_from=datetime.date(1988, 1, 1), content=parent_content, shop=shop)
    children_content = "Children content"
    create_page(content=children_content, parent=page, shop=shop)  # Create invisible children

    assert page.list_children_on_page == False
    check_children_content(request, page, children_content, False)

    page.list_children_on_page = True
    page.save()
    check_children_content(request, page, children_content, False)
