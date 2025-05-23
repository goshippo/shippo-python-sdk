"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LiveRateTypedDict(TypedDict):
    amount: NotRequired[str]
    r"""Final Rate price, expressed in the currency used in the sender's country."""
    amount_local: NotRequired[str]
    r"""Final Rate price, expressed in the currency used in the recipient's country."""
    currency: NotRequired[str]
    r"""Currency used in the sender's country, refers to `amount`.
    The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a> currency codes are used, e.g. `USD` or `EUR`.
    """
    currency_local: NotRequired[str]
    r"""Currency used in the recipient's country, refers to `amount_local`.
    The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a> currency codes are used, e.g. `USD` or \"EUR\".
    """
    estimated_days: NotRequired[int]
    r"""The estimated days in transit of the rate that powers the shipping option, if available."""
    title: NotRequired[str]
    r"""The name of the service group being returned"""


class LiveRate(BaseModel):
    amount: Optional[str] = None
    r"""Final Rate price, expressed in the currency used in the sender's country."""

    amount_local: Optional[str] = None
    r"""Final Rate price, expressed in the currency used in the recipient's country."""

    currency: Optional[str] = None
    r"""Currency used in the sender's country, refers to `amount`.
    The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a> currency codes are used, e.g. `USD` or `EUR`.
    """

    currency_local: Optional[str] = None
    r"""Currency used in the recipient's country, refers to `amount_local`.
    The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a> currency codes are used, e.g. `USD` or \"EUR\".
    """

    estimated_days: Optional[int] = None
    r"""The estimated days in transit of the rate that powers the shipping option, if available."""

    title: Optional[str] = None
    r"""The name of the service group being returned"""
