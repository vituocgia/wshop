/**
 * This file is part of Wshop.
 *
 * Copyright (c) 2012-2018, Shoop Commerce Ltd. All rights reserved.
 *
 * This source code is licensed under the OSL-3.0 license found in the
 * LICENSE file in the root directory of this source tree.
 */
function changeLanguage() {
    const form = document.createElement("form");
    form.method = "POST";
    form.action = window.WshopAdminConfig.browserUrls.setLanguage;
    const input = document.createElement("input");
    input.type = "hidden";
    input.name = "language";
    input.id = "language-field";
    input.value = $(this).data("value");
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
}

$(function(){
    "use strict";
    $(".languages li a").click(changeLanguage);
});