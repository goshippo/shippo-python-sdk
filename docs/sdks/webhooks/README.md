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
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.webhooks.create_webhook(request=components.WebhookUpdateRequest(
    event=components.WebhookEventTypeEnum.BATCH_CREATED,
    url='https://example.com/shippo-webhook',
    active=True,
    is_test=False,
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [components.WebhookUpdateRequest](../../models/components/webhookupdaterequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |

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
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.webhooks.list_webhooks()

if res is not None:
    # handle response
    pass

```

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
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.webhooks.get_webhook(webhook_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `webhook_id`                         | *str*                                | :heavy_check_mark:                   | Object ID of the webhook to retrieve |

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
import shippo
from shippo.models import components

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


res = s.webhooks.update_webhook(webhook_update_request=components.WebhookUpdateRequest(
    event=components.WebhookEventTypeEnum.BATCH_CREATED,
    url='https://example.com/shippo-webhook',
    active=True,
    is_test=False,
), webhook_id='<value>')

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `webhook_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | Object ID of the webhook to retrieve                                               |
| `webhook_update_request`                                                           | [components.WebhookUpdateRequest](../../models/components/webhookupdaterequest.md) | :heavy_check_mark:                                                                 | N/A                                                                                |

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
import shippo

s = shippo.Shippo(
    api_key_header="<YOUR_API_KEY_HERE>",
    shippo_api_version='2018-02-08',
)


s.webhooks.delete_webhook(webhook_id='<value>')

# Use the SDK ...

```

### Parameters

| Parameter                          | Type                               | Required                           | Description                        |
| ---------------------------------- | ---------------------------------- | ---------------------------------- | ---------------------------------- |
| `webhook_id`                       | *str*                              | :heavy_check_mark:                 | Object ID of the webhook to delete |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |