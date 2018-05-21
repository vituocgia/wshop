The Provides system
===================

The Provides system is Wshop's mechanism for discovering and loading
components, both first-party and third-party.  Wshop apps use
the provides system in various ways.

* The core itself uses Provides for discovering method and supplier modules.
* ``wshop.admin`` uses Provides to load admin modules, form customizations etc.
* ``wshop.front`` uses it for URLconf overrides etc.

The provide categories used by Wshop are listed in :ref:`provide-categories` but you
can also define your own categories as you wish.

.. TODO:: Document the various ways better.

Provides are grouped under different categories, such as ``admin_module``,
``xtheme_plugin``, ``front_urls``, etc.

Declaring Provides
------------------

Wshop uses the Django 1.7+ ``AppConfig`` system to declare provides.

Quite simply, a developer needs only include a dict with provide categories as
the keys and lists of loading specs as values for new provides to be discovered.

.. code-block:: python

   class PigeonAppConfig(AppConfig):

       provides = {
           'service_provider_admin_form': [
               'pigeon.admin_forms:PigeonShippingAdminForm',
           ],
       }

.. note:: Some provides also require the class named by the spec string to include
          an ``identifier`` field. Refer to the implementation guides for particular
          functionalities for details.


Blacklisting Provides
---------------------

Wshop also supports blacklisting unwanted provides. This is useful when one want to disable
some features like shipping and payment methods provided by a single app. This way,
it is easy to select which provides should be loaded by Wshop.
To blacklist provides, you need to set a special Django setting named `WSHOP_PROVIDES_BACKLIST`:

.. code-block:: python

   WSHOP_PROVIDES_BACKLIST = {
        'service_provider_admin_form': [
            'pigeon.admin_forms:PigeonShippingAdminForm'
        ]
    }

This will prevent the spec `pigeon.admin_forms:PigeonShippingAdminForm` from category
`service_provider_admin_form` of being loaded.


Using Provides
--------------

Provide management functions are found in the :mod:`wshop.apps.provides` module.

In general, the :obj:`wshop.apps.provides.get_provide_objects` method is your most useful
entry point.

.. _provide-categories:

Provide Categories
------------------

Core
~~~~

``admin_category_form_part``
    Additional ``FormPart`` classes for Category editing. See :doc:`example <../howto/new_tab>`.

``admin_contact_form_part``
    Additional ``FormPart`` classes for Contact editing. See :doc:`example <../howto/new_tab>`.

``admin_contact_group_form_part``
    Additional ``FormPart`` classes for ContactGroup editing. See :doc:`example <../howto/new_tab>`.

``admin_contact_toolbar_action_item``
    Additional ``DropdownItem`` subclass for Contact detail action buttons.

``admin_contact_edit_toolbar_button``
    Additional ``BaseActionButton`` subclasses for Contact edit.
    Subclass init should take current contact as a parameter.

``admin_contact_section``
    Additional ``Section`` subclasses for Contact detail sections.

``admin_extend_create_shipment_form``
    Allows providing extension for shipment creation in admin.
    Should implement the `~wshop.admin.form_modifier.FormModifier` interface.

``admin_extend_attribute_form``
    Allows providing extension for the product attribute form in admin.
    Should implement the `~wshop.admin.form_modifier.FormModifier` interface.

``admin_order_information``
    Additional information rows for Order detail page. Provide objects should inherit
    from `~wshop.admin.modules.orders.utils.OrderInformation` class.

``admin_main_menu_updater``
    Allows updating the Admin Main Menu with new elements. The objects offered through this
    provide should inherit from ``~wshop.core.utils.menu.MainMenuUpdater`` class.

``admin_product_form_part``
    Additional ``FormPart`` classes for Product editing.
    (This is used by pricing modules, for instance.) See :doc:`example <../howto/new_tab>`.

``admin_product_section``
    Additional ``Section`` subclasses for Product edit sections.

``admin_product_toolbar_action_item``
    Additional ``DropdownItem`` subclass for Product edit action buttons.

``admin_shop_form_part``
    Additional ``FormPart`` classes for Shop editing. See :doc:`example <../howto/new_tab>`.

``admin_module``
    Admin module classes. Practically all of the functionality in the admin is built
    via admin modules.

``customer_dashboard_items``
    Classes to parse customer dashboard items from. These are subclasses of
    ``wshop.front.utils.dashboard.DashboardItem``

``discount_module``
    `~wshop.core.pricing.DiscountModule` for pricing system.

``front_extend_product_list_form``
    Allows providing extension for product list form. Should implement the
    `~wshop.front.utils.sorts_and_filters.ProductListFormModifier`
    interface.

``front_service_checkout_phase_provider``
    Allows providing a custom checkout phase for a service (e.g. payment
    method or shipping method). Should implement the
    `~wshop.front.checkout.ServiceCheckoutPhaseProvider` interface.

``front_template_helper_namespace``
    Additional namespaces to install in the ``wshop`` "package" within
    template contexts.
    .. seealso:: :ref:`custom-template-helper-functions`

``admin_order_toolbar_action_item``
    Additional ``DropdownItem`` subclass for Order detail action buttons.
    Current order is passed to subclass init and static method ``visible_for_object``
    is called for the subclass to check whether to actually show the item.

``admin_order_section``
    Additional ``Section`` subclasses for Order detail sections.

``front_menu_extender``
    Additional menu items provided by addons. These should be subclassed from
    `~wshop.xtheme.extenders.FrontMenuExtender`.

``front_product_order_form``
    List of order forms which are subclasses of ``ProductOrderForm``. These forms
    are shown on product detail page in front as well as previews etc.

``front_urls``
    Lists of frontend URLs to be appended to the usual frontend URLs.

``front_urls_post``
    Lists of frontend URLs to be appended to the usual frontend URLs, even after ``front_urls``.
    Most of the time, ``front_urls`` should do.

``front_urls_pre``
    Lists of frontend URLs to be prepended to the usual frontend URLs.
    Most of the time, ``front_urls`` should do.

``notify_action``
    Notification framework `~wshop.notify.Action` classes.

``notify_condition``
    Notification framework `~wshop.notify.Condition` classes.

``notify_event``
    Notification framework `~wshop.notify.Event` classes.

``notify_script_template``
    Notification framework `~wshop.notify.base.ScriptTemplate` classes.

``order_printouts_delivery_extra_fields``
    Additional information rows for order delivery printout. Provide objects should inherit
    from `~wshop.order_printouts.utils.PrintoutDeliveryExtraInformation` class.

``order_source_modifier_module``
    `~wshop.core.order_creator.OrderSourceModifierModule` for modifying
    order source, e.g. in its
    `~wshop.core.order_creator.OrderSource.get_final_lines`.

``pricing_module``
    Pricing module classes; the pricing module in use is set with the ``WSHOP_PRICING_MODULE`` setting.

``service_behavior_component_form``
    Forms for creating service behavior components in Shop Admin.  When
    creating a custom `service behavior component
    <wshop.core.models.ServiceBehaviorComponent>`, provide a form for it
    via this provide.

``service_provider_admin_form``
    Forms for creating service providers in Shop Admin.  When creating a
    custom `service provider <wshop.core.models.ServiceProvider>`
    (e.g. `carrier <wshop.core.models.Carrier>` or `payment processor
    <wshop.core.models.PaymentProcessor>`), provide a form for it via
    this provide.

``carrier_wizard_form_def``
    `Formdefs <wshop.utils.form_group.FormDef>` for creating carriers
    (and their service(s)) through the shop setup wizard.

``payment_processor_wizard_form_def``
    `Formdefs <wshop.utils.form_group.FormDef>` for creating payment processors
    (and their service(s)) through the shop setup wizard.

``product_context_extra``
    Additional context data for the front product views. Provide objects should inherit
    from `~wshop.front.utils.ProductContextExtra` class.

``supplier_module``
    Supplier module classes (deriving from `~wshop.core.suppliers.base.BaseSupplierModule`),
    as used by `~wshop.core.models.Supplier`.

``tax_module``
    Tax module classes; the tax module in use is set with the ``WSHOP_TAX_MODULE`` setting.

``xtheme``
    XTheme themes (full theme sets).

``xtheme_plugin``
    XTheme plugins (that are placed into placeholders within themes).

``xtheme_resource_injection``
    XTheme resources injection function that takes current context and content as parameters.

Campaigns Provide Categories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``campaign_catalog_filter``
    Filters that filter product catalog queryset to find the matching campaigns.

``campaign_context_condition``
    Context Conditions that matches against the current context in shop to see if campaign matches.

``campaign_product_discount_effect_form``
   Form for handling product discount effects of a catalog campaign.
   Should be a ModelForm with its model being a subclass of
   `~wshop.campaigns.models.ProductDiscountEffect`.

``campaign_basket_condition``
    Conditions that matches against the order source or source lines in basket.

``campaign_basket_discount_effect_form``
    Form for handling discount effects of a basket campaign. Should be
    a ModelForm with its model being a subclass of
    `~wshop.campaigns.models.BasketDiscountEffect`.

``campaign_basket_line_effect_form``
    Form for handling line effects of a basket campaign. Should be a
    ModelForm with its model being a subclass of
    `~wshop.campaigns.models.BasketLineEffect`.

Reports Provide Categories
~~~~~~~~~~~~~~~~~~~~~~~~~~

``reports``
    Class to handle report data collection. Should be a subclass of `~wshop.reports.report.WshopReportBase`.

``report_writer_populator``
    List of functions to populate report writers. This allows the creation of custom output formats.
    Should follow the signature of `~wshop.reports.writer.populate_default_writers`.
