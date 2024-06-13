# WebhookPaginatedList


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `next`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | baseurl?page=3&results=10                                      |
| `previous`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | baseurl?page=1&results=10                                      |
| `count`                                                        | *Optional[int]*                                                | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `results`                                                      | List[[components.Webhook](../../models/components/webhook.md)] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |