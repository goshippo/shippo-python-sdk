# FedExConnectExistingOwnAccountParameters

In the case of masked fields, they should be handled carefully.

Fields also must consider: 
- Not providing a *fields* in parameters will not result in a change to any configured value 
- Providing a value in a *masked field* with ****** (exactly 6 asterisks) will not change the configured value 
- Providing *field* with null will clear the configured value 
- Providing *field* with any other value will change the configured value and may affect the behavior of the account.



## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `first_name`                         | *str*                                | :heavy_check_mark:                   | First name of the account holder     |
| `last_name`                          | *str*                                | :heavy_check_mark:                   | Last name of the account holder      |
| `phone_number`                       | *str*                                | :heavy_check_mark:                   | Phone number of the account holder   |
| `from_address_st`                    | *str*                                | :heavy_check_mark:                   | Street address of the account holder |
| `from_address_city`                  | *str*                                | :heavy_check_mark:                   | City of the account holder           |
| `from_address_state`                 | *str*                                | :heavy_check_mark:                   | State of the account holder          |
| `from_address_zip`                   | *str*                                | :heavy_check_mark:                   | Zip code of the account holder       |
| `from_address_country_iso2`          | *str*                                | :heavy_check_mark:                   | Country of the account holder        |