# DryIce

Specify that the package contains Dry Ice (FedEx, Veho, and UPS only).


## Fields

| Field                                                                         | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `contains_dry_ice`                                                            | *Optional[bool]*                                                              | :heavy_minus_sign:                                                            | Mandatory. Specifies that the package contains Dry Ice.                       |
| `weight`                                                                      | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | Mandatory. Units must be in Kilograms. Cannot be greater than package weight. |