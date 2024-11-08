# CarrierParcelTemplates
(*carrier_parcel_templates*)

## Overview

A carrier parcel template represents a package used for shipping that has preset dimensions defined by a carrier. Some examples of a carrier parcel template include USPS Flat Rate Box and Fedex Small Pak. When using a carrier parcel template, the rates returned may be limited to the carrier that provides the box. You can create user parcel templates using a carrier parcel template. Shippo takes the dimensions of the carrier parcel template but you must configure the weight.

<SchemaDefinition schemaRef="#/components/schemas/CarrierParcelTemplate"/>

### Available Operations

* [list](#list) - List all carrier parcel templates
* [get](#get) - Retrieve a carrier parcel templates

## list

List all carrier parcel template objects. <br> Use the following query string params to filter the results as needed. <br>
<ul>
<li>`include=all` (the default). Includes templates from all carriers </li>
<li>`include=user`. Includes templates only from carriers which the user has added (whether or not they're currently enabled) </li>
<li>`include=enabled`. includes templates only for carriers which the user has added and enabled </li>
<li>`carrier=*token*`. filter by specific carrier, e.g. fedex, usps </li>
</ul>

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_parcel_templates.list(carrier='fedex')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        | Example                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `include`                                                          | [Optional[operations.Include]](../../models/operations/include.md) | :heavy_minus_sign:                                                 | filter by user or enabled                                          |                                                                    |
| `carrier`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | filter by specific carrier                                         | fedex                                                              |

### Response

**[components.CarrierParcelTemplateList](../../models/components/carrierparceltemplatelist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Fetches the parcel template information for a specific carrier parcel template, identified by the token.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_parcel_templates.get(carrier_parcel_template_token='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                       | Type                                                            | Required                                                        | Description                                                     |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `carrier_parcel_template_token`                                 | *str*                                                           | :heavy_check_mark:                                              | The unique string representation of the carrier parcel template |

### Response

**[components.CarrierParcelTemplate](../../models/components/carrierparceltemplate.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |