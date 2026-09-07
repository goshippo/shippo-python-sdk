# WebhookEventTypeEnum

Type of event that triggered the webhook.

## Example Usage

```python
from shippo.models.components import WebhookEventTypeEnum

value = WebhookEventTypeEnum.TRANSACTION_CREATED
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `TRANSACTION_CREATED` | transaction_created   |
| `TRANSACTION_UPDATED` | transaction_updated   |
| `TRACK_UPDATED`       | track_updated         |
| `BATCH_CREATED`       | batch_created         |
| `BATCH_PURCHASED`     | batch_purchased       |
| `ALL`                 | all                   |