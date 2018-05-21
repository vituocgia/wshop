# -*- coding: utf-8 -*-
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.utils.translation import ugettext_lazy as _

from wshop import configuration
from wshop.admin.views.wizard import TemplatedWizardFormDef, WizardPane
from wshop.utils import djangoenv

from .forms import BehaviorWizardForm, ContentWizardForm


class ContentWizardPane(WizardPane):
    """
    Wizard Pane to add initial content pages and configure some behaviors of the shop
    """
    identifier = "content"
    icon = "wshop_admin/img/configure.png"
    title = _("Content & Behavior")

    def visible(self):
        return not configuration.get(None, "wizard_content_completed", False)

    def valid(self):
        """
        This pane will be only valid when at least
        SimpleCMS or xTheme or Notify are in INSTALLED APPS
        """
        return (djangoenv.has_installed("wshop.simple_cms") or djangoenv.has_installed("wshop.xtheme") or
                djangoenv.has_installed("wshop.notify"))

    @property
    def text(self):
        cms_xtheme_installed = (djangoenv.has_installed("wshop.simple_cms") or djangoenv.has_installed("wshop.xtheme"))
        notify_installed = djangoenv.has_installed("wshop.notify")

        if cms_xtheme_installed and notify_installed:
            return _("Add the initial content and configure the customer notifications for your shop")
        elif notify_installed:
            return _("Configure notifications for your shop")
        else:
            return _("Add the initial content")

    def get_form_defs(self):
        form_defs = []

        if djangoenv.has_installed("wshop.simple_cms") or djangoenv.has_installed("wshop.xtheme"):
            form_defs.append(
                TemplatedWizardFormDef(
                    name="content",
                    template_name="wshop/admin/content/wizard.jinja",
                    form_class=ContentWizardForm,
                    context={"title": _("Configure the initial content pages")},
                    kwargs={"shop": self.object}
                )
            )

        if djangoenv.has_installed("wshop.notify") and djangoenv.has_installed("wshop.front"):
            form_defs.append(
                TemplatedWizardFormDef(
                    name="behaviors",
                    template_name="wshop/admin/content/wizard.jinja",
                    form_class=BehaviorWizardForm,
                    context={"title": _("Configure some notifications")},
                    kwargs={"shop": self.object}
                )
            )

        return form_defs

    def form_valid(self, form):
        if djangoenv.has_installed("wshop.simple_cms") or djangoenv.has_installed("wshop.xtheme"):
            content_form = form["content"]
            content_form.save()

        if djangoenv.has_installed("wshop.notify"):
            behavior_form = form["behaviors"]
            behavior_form.save()

        configuration.set(None, "wizard_content_completed", True)
