.. image:: https://travis-ci.org/wshop/wshop.svg?branch=master
    :target: https://travis-ci.org/wshop/wshop
.. image:: https://coveralls.io/repos/github/wshop/wshop/badge.svg?branch=master
   :target: https://coveralls.io/github/wshop/wshop?branch=master

Wshop
=====

Wshop is an Open Source E-Commerce Platform based on Django and Python.

https://wshop.com/

Copyright
---------

Copyright (C) 2012-2018 by Shoop Commerce Ltd. <contact@wshop.com>

Wshop is International Registered Trademark & Property of Shoop Commerce Ltd.,
Business ID: FI24815722, Business Address: Aurakatu 12 B, 20100 Turku,
Finland.

CLA
---

Contributor License Agreement is required for any contribution to this
project.  Agreement is signed as a part of pull request process.  See
the CLA.rst file distributed with Wshop.

License
-------

Wshop is published under Open Software License version 3.0 (OSL-3.0).
See the LICENSE file distributed with Wshop.

Some external libraries and contributions bundled with Wshop may be
published under other compatible licenses. For these, please
refer to VENDOR-LICENSES.md file in the source code tree or the licenses
included within each package.

Chat
----

We have a Gitter chat room for Wshop.  Come chat with us!  |Join chat|

.. |Join chat| image:: https://badges.gitter.im/Join%20Chat.svg
   :target: https://gitter.im/wshop/wshop

Getting Started with Wshop development
--------------------------------------

See `Getting Started with Wshop Development
<http://wshop.readthedocs.io/en/latest/howto/getting_started_dev.html>`__.


Contributing to Wshop
---------------------

Interested in contributing to Wshop? Please see our `Contribution Guide
<https://www.wshop.com/contributions/>`__.

Documentation
-------------

Wshop documentation is available online at `Read the Docs
<http://wshop.readthedocs.org/>`__.

Documentation is built with `Sphinx <http://sphinx-doc.org/>`__.

Issue the following commands to build the documentation:

.. code:: sh

    pip install Sphinx  # to install Sphinx
    cd doc && make html

To update the API documentation rst files, e.g. after adding new
modules, use command:

.. code:: sh

    ./generate_apidoc.py
