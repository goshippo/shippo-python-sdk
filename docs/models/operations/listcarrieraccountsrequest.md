# ListCarrierAccountsRequest


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `service_levels`                                                       | *Optional[bool]*                                                       | :heavy_minus_sign:                                                     | Appends the property `service_levels` to each returned carrier account |
| `carrier`                                                              | [Optional[components.Carriers]](../../models/components/carriers.md)   | :heavy_minus_sign:                                                     | Filter the response by the specified carrier                           |
| `account_id`                                                           | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | Filter the response by the specified carrier account Id                |
| `page`                                                                 | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | The page number you want to select                                     |
| `results`                                                              | *Optional[int]*                                                        | :heavy_minus_sign:                                                     | The number of results to return per page (max 100)                     |
| `shippo_api_version`                                                   | *Optional[str]*                                                        | :heavy_minus_sign:                                                     | String used to pick a non-default API version to use                   |