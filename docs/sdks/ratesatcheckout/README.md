# RatesAtCheckout
(*rates_at_checkout*)

## Overview

Rates at checkout is a tool for merchants to display up-to-date shipping estimates based on what's in their customers cart and where they’re shipping to.
Merchants set up curated shipping options for customers in the checkout flow based on data in the shopping cart. The request must include the **to** address and item information. Optional fields are the **from** address and package information. If the optional fields are not included, the service will use the default address and/or package configured for rates at checkout. The response is a list of shipping options based on the Service Group configuration.
(see <a href="#tag/Service-Groups">Service Group configuration</a> for details).
<SchemaDefinition schemaRef="#/components/schemas/LiveRate"/>


# Default Parcel Template
Assign one of your user parcel templates to be the default used when generating Live Rates. This template will be used by default when generating Live Rates, unless you explicitly provide a parcel in the Live Rates request.
<SchemaDefinition schemaRef="#/components/schemas/UserParcelTemplate"/>

### Available Operations

* [create](#create) - Generate a live rates request
* [get_default_parcel_template](#get_default_parcel_template) - Show current default parcel template
* [update_default_parcel_template](#update_default_parcel_template) - Update default parcel template
* [delete_default_parcel_template](#delete_default_parcel_template) - Clear current default parcel template

## create

Initiates a live rates request. Include either the object ID for
an existing address record or a fully formed address object when entering
an address value. You can also enter the object ID of an existing user parcel
template or a fully formed user parcel template object as the parcel value.

### Example Usage

```python
import dateutil.parser
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates_at_checkout.create(request=components.LiveRateCreateRequest(
    address_to=components.AddressCompleteCreateRequest(
        name='Shwan Ippotle',
        street1='215 Clayton St.',
        city='San Francisco',
        state='CA',
        zip='94117',
        country='US',
        company='Shippo',
        street3='',
        street_no='',
        phone='+1 555 341 9393',
        email='shippotle@shippo.com',
        is_residential=True,
        metadata='Customer ID 123456',
        validate=True,
    ),
    line_items=[
        components.LineItem(
            currency='USD',
            manufacture_country='US',
            max_delivery_time=dateutil.parser.isoparse('2016-07-23T00:00:00Z'),
            max_ship_time=dateutil.parser.isoparse('2016-07-23T00:00:00Z'),
            quantity=20,
            sku='HM-123',
            title='Hippo Magazines',
            total_price='12.1',
            variant_title='June Edition',
            weight='0.4',
            weight_unit=components.WeightUnitEnum.LB,
            object_id='abf7d5675d744b6ea9fdb6f796b28f28',
        ),
    ],
    address_from='<value>',
    parcel='5df144dca289442cv7a06',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [components.LiveRateCreateRequest](../../models/components/liveratecreaterequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |

### Response

**[components.LiveRatePaginatedList](../../models/components/liveratepaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_default_parcel_template

Retrieve and display the currently configured default parcel template for live rates.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates_at_checkout.get_default_parcel_template()

if res is not None:
    # handle response
    pass

```

### Response

**[components.DefaultParcelTemplate](../../models/components/defaultparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_default_parcel_template

Update the currently configured default parcel template for live rates. The object_id in the request payload should identify the user parcel template to be the new default.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates_at_checkout.update_default_parcel_template(request=components.DefaultParcelTemplateUpdateRequest(
    object_id='b958d3690bb04bb8b2986724872750f5',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      | Example                          |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `object_id`                      | *Optional[str]*                  | :heavy_minus_sign:               | N/A                              | b958d3690bb04bb8b2986724872750f5 |

### Response

**[components.DefaultParcelTemplate](../../models/components/defaultparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_default_parcel_template

Clears the currently configured default parcel template for live rates.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


s.rates_at_checkout.delete_default_parcel_template()

# Use the SDK ...

```

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |