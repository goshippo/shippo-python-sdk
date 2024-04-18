# RemoveShipmentsFromBatchRequest


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `batch_id`                                             | *str*                                                  | :heavy_check_mark:                                     | Object ID of the batch                                 |
| `request_body`                                         | List[*str*]                                            | :heavy_minus_sign:                                     | Array of shipments object ids to remove from the batch |