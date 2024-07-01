# ListShipmentsRequest


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `page`                                                               | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The page number you want to select                                   |
| `results`                                                            | *Optional[int]*                                                      | :heavy_minus_sign:                                                   | The number of results to return per page (max 100)                   |
| `object_created_gt`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Object(s) created greater than a provided date and time.             |
| `object_created_gte`                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Object(s) created greater than or equal to a provided date and time. |
| `object_created_lt`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Object(s) created lesser than a provided date and time.              |
| `object_created_lte`                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | Object(s) created lesser than or equal to a provided date and time.  |