# TrackingStatus
(*tracking_status*)

## Overview

<p style="text-align: center; background-color: #F2F3F4;"></br>
If you purchased your shipping label through Shippo, you can also get all the tracking details of your Shipment 
from the <a href="#tag/Transactions">Transaction</a> object.
</br></br></p>
A tracking status of a package is an indication of current location of a package in the supply chain. For example,  sorting, warehousing, or out for delivery. Use the tracking status object to track the location of your shipments.

When using your <a href="https://docs.goshippo.com/docs/guides_general/authentication/">Test</a> token for tracking, you need to use Shippo's 
predefined tokens for testing different tracking statuses. You can find more information in our 
<a href="https://docs.goshippo.com/docs/tracking/tracking/">Tracking tutorial</a> on how to do this, and what the 
payloads look like.      
<SchemaDefinition schemaRef="#/components/schemas/Track"/>

### Available Operations

* [create](#create) - Register a tracking webhook
* [get](#get) - Get a tracking status

## create

Registers a webhook that will send HTTP notifications to you when the status of your tracked package changes. For more details on creating a webhook, see our guides on <a href="https://docs.goshippo.com/docs/tracking/webhooks/">Webhooks</a> and <a href="https://docs.goshippo.com/docs/tracking/tracking/">Tracking</a>.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.tracking_status.create(shippo_api_version='2018-02-08', tracks_request=components.TracksRequest(
    carrier='usps',
    tracking_number='9205590164917312751089',
    metadata='Order 000123',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `shippo_api_version`                                                           | *Optional[str]*                                                                | :heavy_minus_sign:                                                             | String used to pick a non-default API version to use                           | 2018-02-08                                                                     |
| `tracks_request`                                                               | [Optional[components.TracksRequest]](../../models/components/tracksrequest.md) | :heavy_minus_sign:                                                             | N/A                                                                            |                                                                                |


### Response

**[components.Track](../../models/components/track.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.BadRequestWithDetail | 400                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get

Returns the tracking status of a shipment using a carrier name and a tracking number.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.tracking_status.get(tracking_number='<value>', carrier='<value>', shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `tracking_number`                                    | *str*                                                | :heavy_check_mark:                                   | Tracking number                                      |                                                      |
| `carrier`                                            | *str*                                                | :heavy_check_mark:                                   | Name of the carrier                                  |                                                      |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


### Response

**[components.Track](../../models/components/track.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.BadRequestWithDetail | 400                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |
