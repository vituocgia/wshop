Getting Started with Wshop Development
======================================

.. note::

   If you are planning on using Wshop to build your own shop,
   read the :doc:`Getting Started with Wshop guide <getting_started>`
   instead.

.. note::

   Interested in contributing to Wshop? Take a look at our `Contribution
   Guide <https://www.wshop.com/en/wshop/contribution-guide>`__.

Requirements
------------
* Python 2.7.9+/3.4+. https://www.python.org/download/.
* Node.js (v0.12 or above). https://nodejs.org/en/download/
* Any database supported by Django.

Installation for Wshop Development
----------------------------------

To start developing Wshop, you'll need a Git checkout of Wshop and a
Github fork of Wshop for creating pull requests.  Github pull requests
are used to get your changes into Wshop Base.

1. If you haven't done so already, create a fork of Wshop in Github by
   clicking the "Fork" button at https://github.com/wshop/wshop and
   clone the fork to your computer as usual. See `Github Help about
   forking repos <https://help.github.com/articles/fork-a-repo/>`__ for
   details.

2. Setup a virtualenv and activate it.  You may use the traditional
   ``virtualenv`` command, or the newer ``python -m venv`` if you're
   using Python 3.  See `Virtualenv User Guide
   <https://virtualenv.pypa.io/en/latest/userguide.html>`__, if you
   are unfamiliar with virtualenv.  For example, following commands
   create and activate a virtualenv in Linux:

   .. code-block:: shell

      virtualenv wshop-venv
      . wshop-venv/bin/activate

3. Finally, you'll need to install Wshop in the activated virtualenv in
   development mode.  To do that, run the following commands in the
   root of the checkout (within the activated virtualenv):

   .. code-block:: shell

      pip install -e .[everything]

Workbench, the built-in test project
------------------------------------

The Workbench project in the repository is a self-contained Django
project set up to use an SQLite database. It is used by the test suite
and is also useful for development on its own.

Practically the only difference to a normal Django project is that instead
of ``python manage.py``, one uses ``python -m wshop_workbench``.

To get started with Workbench, invoke the following in the Wshop working copy
root.

.. code-block:: shell

   # Migrate database.
   python -m wshop_workbench migrate

   # Import some basic data.
   python -m wshop_workbench wshop_populate_mock --with-superuser=admin

   # Run the Django development server (on port 8000 by default).
   python -m wshop_workbench runserver

You can use the credentials ``admin``/``admin``, that is username ``admin``
and password ``admin`` to log in as a superuser on http://127.0.0.1:8000/ .

Building resources
------------------

Wshop uses JavaScript and CSS resources that are compiled using various
Node.js packages.  These resources are compiled automatically by
``setup.py`` when installing Wshop with pip, but if you make changes to
the source files (e.g. under ``wshop/admin/static_src``), the resources
have to be rebuilt.

This can be done with

.. code-block:: shell

   python setup.py build_resources

The command also accepts couple arguments, see its help for more details:

.. code-block:: shell

   python setup.py build_resources --help

Running tests
-------------

To run tests in the active virtualenv:

.. code-block:: shell

   py.test -v --nomigrations wshop_tests
   # Or with coverage
   py.test -vvv --nomigrations --cov wshop --cov-report html wshop_tests

To run tests for all supported Python versions run:

.. code-block:: shell

   pip install tox  # To install tox, needed just once
   tox

Running browser tests
---------------------

.. code-block:: shell

   WSHOP_BROWSER_TESTS=1 py.test -v --nomigrations wshop_tests/browser

Headless with Firefox:

.. code-block:: shell

   WSHOP_BROWSER_TESTS=1 MOZ_HEADLESS=1 py.test -v --nomigrations wshop_tests/browser

For Chrome

.. code-block:: shell

   WSHOP_BROWSER_TESTS=1 py.test -v --nomigrations --splinter-webdriver=chrome wshop_tests/browser


For OSX with Homebrew:

.. code-block:: shell

    # Install Chrome driver (tested with 2.34.522932 (4140ab217e1ca1bec0c4b4d1b148f3361eb3a03e)
    brew install chromedriver

    # Install Geckodriver (for Firefox)
    brew install geckodriver

    # If your current version is below 0.19.1 (for Firefox)
    brew upgrade geckodriver

    # Make sure the selenium is up to date (tested with 3.8.0)
    pip install selenium -U

    # Make sure splinter is up to date (tested with 0.7.6)
    pip install splinter -U

For other OS and browsers check package documentation directly:
* `Geckodriver <https://github.com/mozilla/geckodriver>`__
* `Selenium <https://github.com/SeleniumHQ/selenium>`__
* `Splinter <https://github.com/cobrateam/splinter>`__

Warning! There is inconsistency issues with browser tests and if you suspect your
changes did not break the tests we suggest you rerun the test before
starting debugging more.

Known issues:
* With Chrome test `wshop_tests/browser/front/test_checkout_with_login_and_register.py`
is very unstable.

Collecting translatable messages
--------------------------------

To update the PO catalog files which contain translatable (and
translated) messages, issue ``wshop_makemessages`` management command in
the ``wshop`` directory:

.. code-block:: shell

   cd wshop && python -m wshop_workbench wshop_makemessages
