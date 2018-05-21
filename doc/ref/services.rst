Services API
============

Wshop provides a service API which is based on polymorphic models.
Currently Wshop provides two implementations of these services: `payment
methods <wshop.core.models.PaymentMethod>` and `shipping methods
<wshop.core.models.ShippingMethod>`, but the API allows implementing
other kind of services too.

From the Services API point of view a `service
<wshop.core.models.Service>` is something that may conditionally
`generate some new lines <wshop.core.models.Service.get_lines>` for a
basket.  Also various aspects of these services can be customized:

  * `Availability <wshop.core.models.Service.is_available_for>` of the
    service for certain basket
  * `Costs <wshop.core.models.Service.get_costs>` of the service for
    certain basket
  * `Effective name <wshop.core.models.Service.get_effective_name>` of
    the service for certain basket

Each service should have a `service provider
<wshop.core.models.ServiceProvider>` and `service choice
<wshop.core.models.ServiceChoice>`, which is selected from a list of
service choices specified by the service provider.

Behavior of a service can be customized with `behavior components
<wshop.core.models.ServiceBehaviorComponent>`.  Each behavior component
may limit availability of the service, or (conditionally) add costs to
it, or affect service delivery time (which in case of shipping methods
is the shipping time, but could have other meaning for other kinds of
services).  It is possible to assign several behavior components to a
service.
