# CustomsInvoicedCharges

Additional invoiced charges to be shown on the Customs Declaration Commercial Invoice.


## Fields

| Field                                                                   | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `currency`                                                              | *str*                                                                   | :heavy_check_mark:                                                      | Currency for the invoiced charges amounts incurred on the end consumer. |
| `total_shipping`                                                        | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Total shipping paid by the buyer.                                       |
| `total_taxes`                                                           | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Total taxes paid by the buyer.                                          |
| `total_duties`                                                          | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Total duties paid by the buyer.                                         |
| `other_fees`                                                            | *Optional[str]*                                                         | :heavy_minus_sign:                                                      | Other fees paid by the buyer.                                           |