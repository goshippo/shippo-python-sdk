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
* [initiate_oauth2_signin](#initiate_oauth2_signin) - Connect an existing carrier account using OAuth 2.0
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
    shippo_api_version='2018-02-08',
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
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.create(shippo_api_version='2018-02-08', connect_existing_own_account_request=components.ConnectExistingOwnAccountRequest(
    account_id='321123',
    carrier='fedex',
    parameters={
        'key': '<value>',
    },
    metadata='FEDEX Account',
    test=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          | Example                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                 | *Optional[str]*                                                                                                      | :heavy_minus_sign:                                                                                                   | String used to pick a non-default API version to use                                                                 | 2018-02-08                                                                                                           |
| `connect_existing_own_account_request`                                                                               | [Optional[components.ConnectExistingOwnAccountRequest]](../../models/components/connectexistingownaccountrequest.md) | :heavy_minus_sign:                                                                                                   | Examples.                                                                                                            |                                                                                                                      |


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
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.get(carrier_account_id='<value>', shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                            | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `carrier_account_id`                                 | *str*                                                | :heavy_check_mark:                                   | Object ID of the carrier account                     |                                                      |
| `shippo_api_version`                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | String used to pick a non-default API version to use | 2018-02-08                                           |


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
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.update(carrier_account_id='<value>', shippo_api_version='2018-02-08', carrier_account_base=components.CarrierAccountBase(
    account_id='****',
    carrier='usps',
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              | Example                                                                                  |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `carrier_account_id`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Object ID of the carrier account                                                         |                                                                                          |
| `shippo_api_version`                                                                     | *Optional[str]*                                                                          | :heavy_minus_sign:                                                                       | String used to pick a non-default API version to use                                     | 2018-02-08                                                                               |
| `carrier_account_base`                                                                   | [Optional[components.CarrierAccountBase]](../../models/components/carrieraccountbase.md) | :heavy_minus_sign:                                                                       | Examples.                                                                                |                                                                                          |


### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |

## initiate_oauth2_signin

Used by client applications to setup or reconnect an existing carrier account with carriers that support OAuth 2.0

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.initiate_oauth2_signin(carrier_account_object_id='<value>', redirect_uri='http://fine-cummerbund.biz', state='<value>', shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    | Example                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `carrier_account_object_id`                                                                                                                                                                                    | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | The carrier account ID to start a signin process                                                                                                                                                               |                                                                                                                                                                                                                |
| `redirect_uri`                                                                                                                                                                                                 | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | Callback URL. The URL that tells the authorization server where to send the user back to after they approve the request.                                                                                       |                                                                                                                                                                                                                |
| `state`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | A random string generated by the consuming application and included in the request to prevent CSRF attacks. The consuming application checks that the same value is returned after the user authorizes Shippo. |                                                                                                                                                                                                                |
| `shippo_api_version`                                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | String used to pick a non-default API version to use                                                                                                                                                           | 2018-02-08                                                                                                                                                                                                     |


### Response

**[operations.InitiateOauth2SigninResponse](../../models/operations/initiateoauth2signinresponse.md)**
### Errors

| Error Object                                                   | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.InitiateOauth2SigninResponseBody                        | 400                                                            | application/json                                               |
| errors.InitiateOauth2SigninCarrierAccountsResponseBody         | 401                                                            | application/json                                               |
| errors.InitiateOauth2SigninCarrierAccountsResponseResponseBody | 422                                                            | application/json                                               |
| errors.SDKError                                                | 4xx-5xx                                                        | */*                                                            |

## register

Adds a Shippo carrier account

### Example Usage

```python
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.register(shippo_api_version='2018-02-08', request_body=components.CarrierAccountColissimoCreateRequest(
    carrier='colissimo',
    parameters=components.CarrierAccountColissimoCreateRequestParameters(),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `shippo_api_version`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String used to pick a non-default API version to use                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 2018-02-08                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `request_body`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [Optional[Union[components.CarrierAccountCanadaPostCreateRequest, components.CarrierAccountChronopostCreateRequest, components.CarrierAccountColissimoCreateRequest, components.CarrierAccountCorreosCreateRequest, components.CarrierAccountDeutschePostCreateRequest, components.CarrierAccountDHLExpressCreateRequest, components.CarrierAccountDpdDeCreateRequest, components.CarrierAccountDPDUKCreateRequest, components.CarrierAccountFedExCreateRequest, components.CarrierAccountHermesUKCreateRequest, components.CarrierAccountMondialRelayCreateRequest, components.CarrierAccountPosteItalianeCreateRequest, components.CarrierAccountUPSCreateRequest, components.CarrierAccountUSPSCreateRequest]]](../../models/operations/registercarrieraccountrequestbody.md) | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Examples.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |


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
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.get_registration_status(carrier=operations.Carrier.USPS, shippo_api_version='2018-02-08')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `carrier`                                                | [operations.Carrier](../../models/operations/carrier.md) | :heavy_check_mark:                                       | filter by specific carrier                               |                                                          |
| `shippo_api_version`                                     | *Optional[str]*                                          | :heavy_minus_sign:                                       | String used to pick a non-default API version to use     | 2018-02-08                                               |


### Response

**[components.CarrierAccountRegistrationStatus](../../models/components/carrieraccountregistrationstatus.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
