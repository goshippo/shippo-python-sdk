# AddShipmentsToBatchRequest


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `batch_id`                                                                         | *str*                                                                              | :heavy_check_mark:                                                                 | Object ID of the batch                                                             |
| `request_body`                                                                     | List[[components.BatchShipmentBase](../../models/components/batchshipmentbase.md)] | :heavy_check_mark:                                                                 | Array of shipments to add to the batch                                             |