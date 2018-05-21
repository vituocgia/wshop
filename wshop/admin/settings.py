# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

"""
Settings of Wshop Admin.

See :ref:`apps-settings` (in :obj:`wshop.apps`) for general information
about the Wshop settings system.  Especially, when inventing settings of
your own, the :ref:`apps-naming-settings` section is an important read.
"""

#: Spec which defines a list of Wizard Panes to be shown in Wshop Admin
#: for Wshop initialization and configuration.
#:
#: Panes must be subclasses of `wshop.admin.views.WizardPane`.
#:
WSHOP_SETUP_WIZARD_PANE_SPEC = []

#: Spec which defines a function that loads and return discovered admin modules.
#: This function should return a list of `wshop.admin.base.AdminModule`
#:
WSHOP_GET_ADMIN_MODULES_SPEC = ("wshop.admin.module_registry.get_admin_modules")

#: Spec which defines the Shop provider.
#: The shop provider is the interface responsible for fetching and setting
#: the active shop in admin module
#:
WSHOP_ADMIN_SHOP_PROVIDER_SPEC = ("wshop.admin.shop_provider.AdminShopProvider")
