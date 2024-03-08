# BatchShipmentListWrapper

Array of <a href="#section/Batch-Shipment">BatchShipment</a> objects. 
The response keeps the same order as in the request array.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `next`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | baseurl?page=3&results=10                                                  |
| `previous`                                                                 | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        | baseurl?page=1&results=10                                                  |
| `results`                                                                  | List[[components.BatchShipment](../../models/components/batchshipment.md)] | :heavy_minus_sign:                                                         | N/A                                                                        |                                                                            |