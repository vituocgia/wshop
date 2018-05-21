/**
 * This file is part of Wshop.
 *
 * Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
var gutil = require("gulp-util");
var path = require("path");

module.exports.DEST_DIR = path.join("static", "wshop_admin");
module.exports.PRODUCTION = gutil.env.production || (process.env.NODE_ENV === "production");
module.exports.WATCH = !!gutil.env.watch;
