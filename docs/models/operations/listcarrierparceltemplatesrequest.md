# ListCarrierParcelTemplatesRequest


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `include`                                                          | [Optional[operations.Include]](../../models/operations/include.md) | :heavy_minus_sign:                                                 | filter by user or enabled                                          |
| `carrier`                                                          | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | filter by specific carrier                                         |
| `shippo_api_version`                                               | *Optional[str]*                                                    | :heavy_minus_sign:                                                 | String used to pick a non-default API version to use               |