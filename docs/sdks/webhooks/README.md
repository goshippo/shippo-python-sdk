# Webhooks
(*webhooks*)

## Overview

Webhooks are a way for Shippo to notify your application when a specific event occurs. For example, when a label is purchased or when a shipment tracking status has changed. You can use webhooks to trigger actions in your application, such as sending an email or updating a database.
<SchemaDefinition schemaRef="#/components/schemas/Webhook"/>

# Webhook Payload
The payload is the body of the POST request Shippo sends to the URL specified at the time of webhook registration.
<SchemaDefinition schemaRef="#/components/schemas/WebhookPayload"/>

### Available Operations

* [create_webhook](#create_webhook) - Create a new webhook
* [list_webhooks](#list_webhooks) - List all webhooks
* [get_webhook](#get_webhook) - Retrieve a specific webhook
* [update_webhook](#update_webhook) - Update an existing webhook
* [delete_webhook](#delete_webhook) - Delete a specific webhook

## create_webhook

Creates a new webhook to send notifications to a URL when a specific event occurs.

### Example Usage

```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.webhooks.create_webhook(request={
        "event": components.WebhookEventTypeEnum.BATCH_CREATED,
        "url": "https://example.com/shippo-webhook",
        "active": True,
        "is_test": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.WebhookUpdateRequest](../../models/components/webhookupdaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[components.Webhook](../../models/components/webhook.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## list_webhooks

Returns a list of all webhooks you have created.

### Example Usage

```python
from shippo import Shippo


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.webhooks.list_webhooks()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.WebhookPaginatedList](../../models/components/webhookpaginatedlist.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## get_webhook

Returns the details of a specific webhook using the webhook object ID.

### Example Usage

```python
from shippo import Shippo


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.webhooks.get_webhook(webhook_id="<id>")

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the webhook to retrieve                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[components.Webhook](../../models/components/webhook.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## update_webhook

Updates an existing webhook using the webhook object ID.

### Example Usage

```python
from shippo import Shippo
from shippo.models import components


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    res = s_client.webhooks.update_webhook(webhook_id="<id>", webhook_update_request={
        "event": components.WebhookEventTypeEnum.BATCH_CREATED,
        "url": "https://example.com/shippo-webhook",
        "active": True,
        "is_test": False,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `webhook_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | Object ID of the webhook to retrieve                                               |
| `webhook_update_request`                                                           | [components.WebhookUpdateRequest](../../models/components/webhookupdaterequest.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[components.Webhook](../../models/components/webhook.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |

## delete_webhook

Deletes a specific webhook using the webhook object ID.

### Example Usage

```python
from shippo import Shippo


with Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version="2018-02-08",
) as s_client:

    s_client.webhooks.delete_webhook(webhook_id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | Object ID of the webhook to delete                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |