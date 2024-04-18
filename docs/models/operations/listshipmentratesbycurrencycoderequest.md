# ListShipmentRatesByCurrencyCodeRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `shipment_id`                                      | *str*                                              | :heavy_check_mark:                                 | Object ID of the shipment to update                |
| `currency_code`                                    | *str*                                              | :heavy_check_mark:                                 | ISO currency code for the rates                    |
| `page`                                             | *Optional[int]*                                    | :heavy_minus_sign:                                 | The page number you want to select                 |
| `results`                                          | *Optional[int]*                                    | :heavy_minus_sign:                                 | The number of results to return per page (max 100) |