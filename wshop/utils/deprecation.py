#!/usr/bin/env python
# This file is part of Wshop.
#
# Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.


class RemovedInWshop20Warning(PendingDeprecationWarning):
    pass


class RemovedFromWshopWarning(DeprecationWarning):
    pass


RemovedInFutureWshopWarning = RemovedInWshop20Warning
