# UPSConnectExistingOwnAccountStreamlinedParameters

Streamlined alternative to the full UPS account parameters. Provide only the UPS account number, the billing country, and acceptance of the UPS terms. Contact, billing address, and invoice details are not required with this format.
The full UPS account parameters format is also supported.

To protect account information, this field will be masked in any API response.
In the case of masked fields, they should be handled carefully.

Fields also must consider: 
- Not providing a *fields* in parameters will not result in a change to any configured value 
- Providing a value in a *masked field* with ****** (exactly 6 asterisks) will not change the configured value 
- Providing *field* with null will clear the configured value 
- Providing *field* with any other value will change the configured value and may affect the behavior of the account.


## Fields

| Field                                                                                                            | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      | Example                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `account_number`                                                                                                 | *str*                                                                                                            | :heavy_check_mark:                                                                                               | The UPS account number                                                                                           | 1989                                                                                                             |
| `billing_address_country_iso2`                                                                                   | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Two-letter ISO 3166-1 country code of the billing address on the UPS account                                     | BE                                                                                                               |
| `ups_agreements`                                                                                                 | *bool*                                                                                                           | :heavy_check_mark:                                                                                               | Whether the user agrees to the UPS terms and conditions or not. Error 400 will be returned if passed in as false |                                                                                                                  |