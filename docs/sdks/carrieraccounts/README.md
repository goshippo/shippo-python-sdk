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


res = s.carrier_accounts.list(request=operations.ListCarrierAccountsRequest())

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

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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


res = s.carrier_accounts.create(request=components.ConnectExistingOwnAccountRequest(
    account_id='321123',
    carrier='fedex',
    parameters=components.FedExConnectExistingOwnAccountParameters(
        first_name='Loyal',
        last_name='Collier',
        phone_number='(890) 307-8579',
        from_address_st='<value>',
        from_address_city='<value>',
        from_address_state='<value>',
        from_address_zip='<value>',
        from_address_country_iso2='<value>',
    ),
    metadata='FEDEX Account',
    test=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [components.ConnectExistingOwnAccountRequest](../../models/components/connectexistingownaccountrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |

### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get

Returns an existing carrier account using an object ID.

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.get(carrier_account_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `carrier_account_id`             | *str*                            | :heavy_check_mark:               | Object ID of the carrier account |

### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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


res = s.carrier_accounts.update(carrier_account_id='<value>', carrier_account_base=components.CarrierAccountBase(
    account_id='****',
    carrier='usps',
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
        ups_agreements=True,
        aia_country_iso2='US',
        billing_address_street2='STE 200',
        currency_code='USD',
        invoice_controlid='1234',
        invoice_date='20210529',
        invoice_number='1112234',
        invoice_value='11.23',
    ),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `carrier_account_id`                                                                     | *str*                                                                                    | :heavy_check_mark:                                                                       | Object ID of the carrier account                                                         |
| `carrier_account_base`                                                                   | [Optional[components.CarrierAccountBase]](../../models/components/carrieraccountbase.md) | :heavy_minus_sign:                                                                       | Examples.                                                                                |

### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## initiate_oauth2_signin

Used by client applications to setup or reconnect an existing carrier account with carriers that support OAuth 2.0

### Example Usage

```python
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.carrier_accounts.initiate_oauth2_signin(carrier_account_object_id='<value>', redirect_uri='https://enlightened-mortise.com/')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                                      | Type                                                                                                                                                                                                           | Required                                                                                                                                                                                                       | Description                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `carrier_account_object_id`                                                                                                                                                                                    | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | The carrier account ID (UUID) to start a signin process.                                                                                                                                                       |
| `redirect_uri`                                                                                                                                                                                                 | *str*                                                                                                                                                                                                          | :heavy_check_mark:                                                                                                                                                                                             | Callback URL. The URL that tells the authorization server where to send the user back to after they approve the request.                                                                                       |
| `state`                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                             | A random string generated by the consuming application and included in the request to prevent CSRF attacks. The consuming application checks that the same value is returned after the user authorizes Shippo. |

### Response

**[operations.InitiateOauth2SigninResponse](../../models/operations/initiateoauth2signinresponse.md)**

### Errors

| Error Type                                                     | Status Code                                                    | Content Type                                                   |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| errors.InitiateOauth2SigninResponseBody                        | 400                                                            | application/json                                               |
| errors.InitiateOauth2SigninCarrierAccountsResponseBody         | 401                                                            | application/json                                               |
| errors.InitiateOauth2SigninCarrierAccountsResponseResponseBody | 404                                                            | application/json                                               |
| errors.SDKError                                                | 4XX, 5XX                                                       | \*/\*                                                          |

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


res = s.carrier_accounts.register(request=components.CarrierAccountUPSCreateRequest(
    carrier='ups',
    parameters=components.CarrierAccountUPSCreateRequestParameters(
        billing_address_city='San Francisco',
        billing_address_country_iso2='US',
        billing_address_state='CA',
        billing_address_street1='731 Market St',
        billing_address_zip='94103',
        pickup_address_city='San Francisco',
        pickup_address_country_iso2='US',
        pickup_address_state='CA',
        pickup_address_street1='731 Market St',
        pickup_address_zip='94103',
        ups_agreements=True,
        billing_address_street2='STE 200',
        company='Shippo',
        email='hippo@shippo.com',
        full_name='Shippo Meister',
        phone='1112223333',
        pickup_address_same_as_billing_address=False,
        pickup_address_street2='STE 200',
    ),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.RegisterCarrierAccountRequestBody](../../models/operations/registercarrieraccountrequestbody.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |

### Response

**[components.CarrierAccount](../../models/components/carrieraccount.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

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


res = s.carrier_accounts.get_registration_status(carrier=operations.Carrier.USPS)

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `carrier`                                                | [operations.Carrier](../../models/operations/carrier.md) | :heavy_check_mark:                                       | filter by specific carrier                               |

### Response

**[components.CarrierAccountRegistrationStatus](../../models/components/carrieraccountregistrationstatus.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |