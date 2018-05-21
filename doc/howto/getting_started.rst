Installing Wshop
================

.. note::

   If you are planning on developing Wshop,
   read the :doc:`Getting Started with Wshop Development guide
   <getting_started_dev>` instead.

Requirements
------------

* Python 2.7.9+/3.4+. https://www.python.org/download/.
* Any database supported by Django.

Installation
------------

This guide assumes familiarity with the PyPA tools for Python packaging,
including ``pip`` and ``virtualenv``.

1. Update pip and setuptools

   .. code-block:: shell

      pip install -U pip
      pip install -U setuptools

2. Set up a new virtualenv for Wshop and activate it

   .. code-block:: shell

      virtualenv wshop-venv
      . wshop-venv/bin/activate

3. Install wshop via pypi

   .. code-block:: shell

      pip install wshop


4. Once installed, you can begin setting up a Django project using whichever
   standards you fancy. Refer to the top-level `settings
   <https://github.com/wshop/wshop/blob/master/wshop_workbench/settings/base_settings.py>`_
   and `urls
   <https://github.com/wshop/wshop/blob/master/wshop_workbench/urls.py>`_
   for configuration details. At minimum, you will need to add ``wshop.core``
   to your ``INSTALLED_APPS``.

.. note::
   Wshop uses ``django-parler`` for model translations. Please ensure
   ``PARLER_DEFAULT_LANGUAGE_CODE`` is set. See `django-parler configuration
   <http://django-parler.readthedocs.io/en/latest/configuration.html>`_ for more
   details.

.. note::
   Wshop uses the ``LANGUAGES`` setting to render multilingual forms. You'll likely
   want to override this setting to restrict your applications supported languages.

5. Once you have configured the Wshop apps you would like to use, run the
   following commands to create the database and initialize Wshop

   .. code-block:: shell

      python manage.py migrate
      python manage.py wshop_init

Wshop Packages
--------------

Wshop is a constellation of Django apps, with many delivered in the single
"Wshop Base" distribution, and with additional apps available as separate
downloads.

``wshop.core`` is the core package required by all Wshop installations.
It contains the core business logic for e-commerce, and all of the database
models required. However, it contains no frontend or admin dashboard, as
different projects may wish to replace them with other components or even
elide them altogether.

``wshop.front`` is a basic but fully featured storefront. It itself has
several sub-applications that may be used to toggle functionality on and off.

* ``wshop.front.apps.auth`` is a wrapper around django auth for login and
  password recovery.
* ``wshop.front.apps.registration`` provides views for customer activation
  and registration.
* ``wshop.front.apps.customer_information`` provides views for customer
  address management.
* ``wshop.front.apps.personal_order_history`` adds views for customer
  order history.
*  ``wshop.front.apps.simple_order_notification`` can be used to send
   email notifications to the customer upon order completion.
* ``wshop.front.apps.simple_search`` provides basic product search
  functionality.
* ``wshop.front.apps.recently_viewed_products`` can be used to display the last
  five products viewed by the customer.

``wshop.admin`` provides a fully featured administration dashboard.

``wshop.addons`` can be used to install and manage Wshop addons.

``wshop.api`` exposes WSHOP APIs as RESTful url endpoints. See the
:doc:`web API documentation <../web_api>` for details.

``wshop.campaigns`` provides a highly customizable promotion and discount
management system.

``wshop.customer_group_pricing`` can be used to customize product pricing by
customer contact groups.

``wshop.default_tax`` is a rules-based tax module that calculates and applies
taxes on orders. See the :doc:`prices and taxes documentation
<../ref/prices_and_taxes>` for details.

``wshop.guide`` integrates search results from this documentation into Admin
search.

``wshop.notify`` is a generic notification framework that can be used to
inform users about various events (order creation, shipments, password
resets, etc). See the :doc:`notification documentation
<../ref/notify_specification>` for details.

``wshop.order_printouts`` adds support to create PDF printouts of orders from
admin.

``wshop.simple_cms`` is a basic content management system that can be used to
add pages to the storefront.

``wshop.simple_supplier`` is a simple inventory management system that can be
used to keep track of product inventory.
