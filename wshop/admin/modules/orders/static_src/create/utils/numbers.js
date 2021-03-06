/**
 * This file is part of Wshop.
 *
 * Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function ensureNumericValue(value, defaultValue = 0, asInteger = false) {
    if (!isNumeric(value)) {
        return defaultValue || 0;
    }
    if (Number.isInteger(value) || asInteger) {
        return parseInt(value, 10);
    }
    return parseFloat(value).toFixed(2);
}

export default ensureNumericValue;
