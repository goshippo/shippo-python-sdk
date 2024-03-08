# AddShipmentsToBatchRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `batch_id`                                                                         | *str*                                                                              | :heavy_check_mark:                                                                 | Object ID of the batch                                                             |
| `shippo_api_version`                                                               | *Optional[str]*                                                                    | :heavy_minus_sign:                                                                 | String used to pick a non-default API version to use                               |
| `request_body`                                                                     | List[[components.BatchShipmentBase](../../models/components/batchshipmentbase.md)] | :heavy_minus_sign:                                                                 | Array of shipments to add to the batch                                             |