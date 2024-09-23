# Rates
(*rates*)

## Overview

A rate is the cost to ship a parcel from a carrier. The rate object details the service level including the cost and transit time. 
<SchemaDefinition schemaRef="#/components/schemas/Rate"/>

### Available Operations

* [get](#get) - Retrieve a rate
* [list_shipment_rates](#list_shipment_rates) - Retrieve shipment rates
* [list_shipment_rates_by_currency_code](#list_shipment_rates_by_currency_code) - Retrieve shipment rates in currency

## get

Returns an existing rate using a rate object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates.get(rate_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter             | Type                  | Required              | Description           |
| --------------------- | --------------------- | --------------------- | --------------------- |
| `rate_id`             | *str*                 | :heavy_check_mark:    | Object ID of the rate |

### Response

**[components.Rate](../../models/components/rate.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## list_shipment_rates

Returns a paginated list of rates associated with a shipment

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates.list_shipment_rates(shipment_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `shipment_id`                                      | *str*                                              | :heavy_check_mark:                                 | Object ID of the shipment to update                |
| `page`                                             | *Optional[int]*                                    | :heavy_minus_sign:                                 | The page number you want to select                 |
| `results`                                          | *Optional[int]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |

### Response

**[components.RatePaginatedList](../../models/components/ratepaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |


## list_shipment_rates_by_currency_code

Returns all available shipping rates for a shipment object.

When you create a new valid shipment object, Shippo automatically calculates all available rates. Depending on your shipment data, there may be none, one or multiple rates.

By default, the calculated rates will return the price in two currencies under the `amount` and `amount_local` keys, respectively. The `amount` key will contain the price of a rate expressed in the currency that is used in the country from where the parcel originates, and the `amount_local` key will contain the price expressed in the currency that is used in the country the parcel is shipped to. You can request rates with prices expressed in a different currency by adding the currency code to the end of the resource URL. The full list of supported currencies along with their codes can be viewed on <a href="http://openexchangerates.org/api/currencies.json">open exchange rates</a>.

Note: re-requesting the rates with a different currency code will re-queue the shipment (i.e. set the Shipment's `status` to `QUEUED`) and the converted currency rates will only be available when the Shipment's `status` is set to `SUCCESS`.

### Example Usage

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.rates.list_shipment_rates_by_currency_code(request=operations.ListShipmentRatesByCurrencyCodeRequest(
    shipment_id='<value>',
    currency_code='USD',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.ListShipmentRatesByCurrencyCodeRequest](../../models/operations/listshipmentratesbycurrencycoderequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |

### Response

**[components.RatePaginatedList](../../models/components/ratepaginatedlist.md)**

### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
