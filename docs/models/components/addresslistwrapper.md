# AddressListWrapper

Paginated Address Response.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `next`                                                         | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | baseurl?page=3&results=10                                      |
| `previous`                                                     | *Optional[str]*                                                | :heavy_minus_sign:                                             | N/A                                                            | baseurl?page=1&results=10                                      |
| `results`                                                      | List[[components.Address](../../models/components/address.md)] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |