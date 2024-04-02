# CarrierAccounts
(*carrier_accounts*)

## Overview

Carriers are the companies who deliver your package. Shippo uses Carrier account objects as credentials to retrieve shipping rates and purchase labels from shipping Carriers.

<SchemaDefinition schemaRef="#/components/schemas/CarrierAccount"/>

### Available Operations

* [list](#list) - List all carrier accounts
* [create](#create) - Create a new carrier account
* [get](#get) - Retrieve a carrier account
* [update](#update) - Update a carrier account
* [register](#register) - Add a Shippo carrier account
* [get_registration_status](#get_registration_status) - Get Carrier Registration status

## list

Returns a list of all carrier accounts connected to your Shippo account. These carrier accounts include both Shippo carrier accounts and your own carrier accounts that you have connected to your Shippo account.

Additionally, you can get information about the service levels associated with each carrier account by passing in the `?service_levels=true` query parameter. <br>
Using it appends the property `service_levels` to each carrier account. <br>
By default, if the query parameter is omitted, the `service_levels` property will not be included in the response.

### Example Usage

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)

req = operations.ListCarrierAccountsRequest()

res = s.carrier_accounts.list(req)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListCarrierAccountsRequest](../../models/operations/listcarrieraccountsrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[components.CarrierAccountPaginatedList](../../models/components/carrieraccountpaginatedlist.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## create

Creates a new carrier account or connects an existing carrier account to the Shippo account.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.carrier_accounts.create(shippo_api_version='<value>', connect_existing_own_ups_account_request=components.ConnectExistingOwnUPSAccountRequest(
    account_id='<value>',
    active=False,
    parameters=components.UPSConnectExistingOwnAccountParameters(
        account_number='94567e',
        billing_address_city='San Francisco',
        billing_address_country_iso2='US',
        billing_address_state='CA',
        billing_address_street1='731 Market St',
        billing_address_zip='94103',
        collec_country_iso2='US',
        collec_zip='94103',
        company='Shippo',
        email='hippo@shippo.com',
        full_name='Shippo Meister',
        has_invoice=False,
        phone='1112223333',
        title='Manager',
        ups_agreements=False,
        aia_country_iso2='US',
        billing_address_street2='STE 200',
        currency_code='USD',
        invoice_controlid='1234',
        invoice_date='20210529',
        invoice_number='1112234',
        invoice_value='11.23',
    ),
    carrier='ups',
    metadata='UPS Account',
    test=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                       | *Optional[str]*                                                                                                            | :heavy_minus_sign:                                                                                                         | String used to pick a non-default API version to use                                                                       |
| `connect_existing_own_ups_account_request`                                                                                 | [Optional[components.ConnectExistingOwnUPSAccountRequest]](../../models/components/connectexistingownupsaccountrequest.md) | :heavy_minus_sign:                                                                                                         | Examples.                                                                                                                  |


### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**
### Errors

| Error Object                | Status Code                 | Content Type                |
| --------------------------- | --------------------------- | --------------------------- |
| errors.BadRequestWithDetail | 400                         | application/json            |
| errors.SDKError             | 4xx-5xx                     | */*                         |

## get

Returns an existing carrier account using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.carrier_accounts.get(carrier_account_id='<value>', shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `carrier_account_id`                                 | *str*                                                | :heavy_check_mark:                                   | Object ID of the carrier account                     |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use |


### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## update

Updates an existing carrier account object. The account_id and carrier can't be updated. This is because they form the unique identifier together.

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.carrier_accounts.update(carrier_account_id='<value>', shippo_api_version='<value>', carrier_account_base=components.CarrierAccountBase(
    account_id='****',
    carrier='usps',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `carrier_account_id`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Object ID of the carrier account                                                         |
| `shippo_api_version`                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | String used to pick a non-default API version to use                                     |
| `carrier_account_base`                                                                   | [Optional[components.CarrierAccountBase]](../../models/components/carrieraccountbase.md) | :heavy_minus_sign:                                                                       | Examples.                                                                                |


### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## register

Adds a Shippo carrier account

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.carrier_accounts.register(shippo_api_version='<value>', request_body=components.CarrierAccountColissimoCreateRequest(
    carrier='colissimo',
    parameters=components.CarrierAccountColissimoCreateRequestParameters(),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String used to pick a non-default API version to use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `request_body`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Optional[Union[components.CarrierAccountCanadaPostCreateRequest, components.CarrierAccountChronopostCreateRequest, components.CarrierAccountColissimoCreateRequest, components.CarrierAccountCorreosCreateRequest, components.CarrierAccountDeutschePostCreateRequest, components.CarrierAccountDHLExpressCreateRequest, components.CarrierAccountDpdDeCreateRequest, components.CarrierAccountDPDUKCreateRequest, components.CarrierAccountHermesUKCreateRequest, components.CarrierAccountPosteItalianeCreateRequest, components.CarrierAccountUPSCreateRequest, components.CarrierAccountUSPSCreateRequest]]](../../models/operations/registercarrieraccountrequestbody.md) | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Examples.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |


### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequestWithError | 400                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## get_registration_status

Returns the registration status for the given account for the given carrier

### Example Usage

```python
import shippo
from shippo.models import operations

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
)


res = s.carrier_accounts.get_registration_status(carrier=operations.Carrier.USPS, shippo_api_version='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `carrier`                                                | [operations.Carrier](../../models/operations/carrier.md) | :heavy_check_mark:                                       | filter by specific carrier                               |
| `shippo_api_version`                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | String used to pick a non-default API version to use     |


### Response

**[components.CarrierAccountRegistrationStatus](../../models/components/carrieraccountregistrationstatus.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
