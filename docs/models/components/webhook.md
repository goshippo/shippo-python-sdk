# Webhook


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `event`                                                                               | *str*                                                                                 | :heavy_check_mark:                                                                    | Type of event that triggers the webhook.                                              |
| `url`                                                                                 | *str*                                                                                 | :heavy_check_mark:                                                                    | URL webhook events are sent to.                                                       |
| `active`                                                                              | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Determines whether the webhook is active or not.                                      |
| `is_test`                                                                             | *Optional[bool]*                                                                      | :heavy_minus_sign:                                                                    | Determines whether the webhook is a test webhook or not.                              |
| `object_created`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                  | :heavy_minus_sign:                                                                    | Timestamp of the creation of the webhook.                                             |
| `object_id`                                                                           | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Unique identifier of the webhook. This can be used to retrieve or delete the webhook. |
| `object_updated`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                  | :heavy_minus_sign:                                                                    | Timestamp of the last update of the webhook.                                          |
| `object_owner`                                                                        | *Optional[str]*                                                                       | :heavy_minus_sign:                                                                    | Username of the user who created the webhook.                                         |