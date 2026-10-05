# EmbeddedAuthorization

## Overview

Mint short-lived JSON Web Tokens (JWTs) for client-side applications, so you never ship a
long-lived API token to the browser. Authenticate the request with a Shippo API token or an
OAuth bearer token, then pass the returned token as `Authorization: JWT <JWT_TOKEN>`.
See our [Authentication using JWT guide](https://docs.goshippo.com/docs/guides_general/authentication_using_jwt/) for details.

### Available Operations

* [create](#create) - Create a JWT

## create

Creates a short-lived JSON Web Token (JWT) that client-side applications can use
to authenticate against the Shippo API without exposing a long-lived API token.

Authenticate this request with either a Shippo API token
(`Authorization: ShippoToken <API_TOKEN>`) or an OAuth bearer token
(`Authorization: Bearer <OAUTH_BEARER_TOKEN>`). Platform accounts can mint a token
on behalf of a Managed Shippo Account by setting the `SHIPPO-ACCOUNT-ID` header.

The returned token is valid for 12 hours. Send it on subsequent requests as
`Authorization: JWT <JWT_TOKEN>`.

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateEmbeddedAuthorization" method="post" path="/embedded/authz" -->
```python
from shippo import Shippo
from shippo.models import operations


with Shippo(
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.embedded_authorization.create(security=operations.CreateEmbeddedAuthorizationSecurity(
        api_key_header="<YOUR_API_KEY_HERE>",
    ), embedded_authorization_request={
        "scope": "embedded:carriers",
    }, shippo_account_id="e0b382dc7d754c0ca6358c09d5d2bdf7")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                              | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            | Example                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                             | [operations.CreateEmbeddedAuthorizationSecurity](../../models/operations/createembeddedauthorizationsecurity.md)                       | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |                                                                                                                                        |
| `embedded_authorization_request`                                                                                                       | [components.EmbeddedAuthorizationRequest](../../models/components/embeddedauthorizationrequest.md)                                     | :heavy_check_mark:                                                                                                                     | The scope to request for the token.                                                                                                    |                                                                                                                                        |
| `shippo_account_id`                                                                                                                    | *Optional[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                     | Optional. The object ID of a Managed Shippo Account. Platform accounts set this to<br/>mint a JWT scoped to one of their managed accounts. | e0b382dc7d754c0ca6358c09d5d2bdf7                                                                                                       |
| `retries`                                                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                       | :heavy_minus_sign:                                                                                                                     | Configuration to override the default retry behavior of the client.                                                                    |                                                                                                                                        |

### Response

**[components.EmbeddedAuthorization](../../models/components/embeddedauthorization.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |