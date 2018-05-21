#!/usr/bin/env python
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
import logging
import os
import sys
import warnings

from wshop.utils.deprecation import RemovedInFutureWshopWarning

if __name__ == "__main__":
    if not sys.warnoptions:
        # Route warnings through python logging
        logging.captureWarnings(True)
        # RemovedInFutureWshopWarning is a subclass of PendingDeprecationWarning which
        # is hidden by default, hence we force the "default" behavior
        warnings.simplefilter("default", RemovedInFutureWshopWarning)
    sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + "/.."))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wshop_workbench.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
