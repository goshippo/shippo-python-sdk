"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing_extensions import TypedDict


class FedExConnectExistingOwnAccountParametersTypedDict(TypedDict):
    first_name: str
    r"""First name of the account holder"""
    last_name: str
    r"""Last name of the account holder"""
    phone_number: str
    r"""Phone number of the account holder"""
    from_address_st: str
    r"""Street address of the account holder"""
    from_address_city: str
    r"""City of the account holder"""
    from_address_state: str
    r"""State of the account holder"""
    from_address_zip: str
    r"""Zip code of the account holder"""
    from_address_country_iso2: str
    r"""Country of the account holder"""


class FedExConnectExistingOwnAccountParameters(BaseModel):
    first_name: str
    r"""First name of the account holder"""

    last_name: str
    r"""Last name of the account holder"""

    phone_number: str
    r"""Phone number of the account holder"""

    from_address_st: str
    r"""Street address of the account holder"""

    from_address_city: str
    r"""City of the account holder"""

    from_address_state: str
    r"""State of the account holder"""

    from_address_zip: str
    r"""Zip code of the account holder"""

    from_address_country_iso2: str
    r"""Country of the account holder"""
