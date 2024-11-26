# GetBatchRequest


## Fields

| Field                                                         | Type                                                          | Required                                                      | Description                                                   |
| ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------- |
| `batch_id`                                                    | *str*                                                         | :heavy_check_mark:                                            | Object ID of the batch                                        |
| `page`                                                        | *Optional[int]*                                               | :heavy_minus_sign:                                            | The page number you want to select                            |
| `results`                                                     | *Optional[int]*                                               | :heavy_minus_sign:                                            | The number of results to return per page (max 100, default 5) |