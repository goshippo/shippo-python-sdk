"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .objectstateenum import ObjectStateEnum
from .weightunitenum import WeightUnitEnum
from datetime import datetime
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomsItemTypedDict(TypedDict):
    description: str
    r"""Text description of your item."""
    mass_unit: WeightUnitEnum
    r"""The unit used for weight."""
    net_weight: str
    r"""Total weight of this item, i.e. quantity * weight per item."""
    origin_country: str
    r"""Country of origin of the item. Example: `US` or `DE`.
    All accepted values can be found on the <a href=\"http://www.iso.org/\" target=\"_blank\">Official ISO Website</a>.
    """
    quantity: int
    r"""Quantity of this item in the shipment you send.  Must be greater than 0."""
    value_amount: str
    r"""Total value of this item, i.e. quantity * value per item."""
    value_currency: str
    r"""Currency used for value_amount. The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a>
    currency codes are used, e.g.  `USD` or `EUR`.
    """
    eccn_ear99: NotRequired[str]
    r"""Export Control Classification Number, required on some exports from the United States."""
    metadata: NotRequired[str]
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """
    sku_code: NotRequired[str]
    r"""SKU code of the item, which is required by some carriers."""
    hs_code: NotRequired[str]
    r"""HS code of the item, which is required by some carriers. If `tariff_number` is not provided, `hs_code` will be used.  If both `hs_code` and `tariff_number` are provided, `tariff_number` will be used. 50 character limit."""
    tariff_number: NotRequired[str]
    r"""The tariff number of the item. If `tariff_number` is not provided, `hs_code` will be used. If both `hs_code` and `tariff_number` are provided, `tariff_number` will be used. 12 character limit."""
    object_created: NotRequired[datetime]
    r"""Date and time of object creation."""
    object_id: NotRequired[str]
    r"""Unique identifier of the given object."""
    object_owner: NotRequired[str]
    r"""Username of the user who created the object."""
    object_state: NotRequired[ObjectStateEnum]
    r"""Indicates the validity of the enclosing object"""
    object_updated: NotRequired[datetime]
    r"""Date and time of last object update."""
    test: NotRequired[bool]
    r"""Indicates whether the object has been created in test mode."""


class CustomsItem(BaseModel):
    description: str
    r"""Text description of your item."""

    mass_unit: WeightUnitEnum
    r"""The unit used for weight."""

    net_weight: str
    r"""Total weight of this item, i.e. quantity * weight per item."""

    origin_country: str
    r"""Country of origin of the item. Example: `US` or `DE`.
    All accepted values can be found on the <a href=\"http://www.iso.org/\" target=\"_blank\">Official ISO Website</a>.
    """

    quantity: int
    r"""Quantity of this item in the shipment you send.  Must be greater than 0."""

    value_amount: str
    r"""Total value of this item, i.e. quantity * value per item."""

    value_currency: str
    r"""Currency used for value_amount. The <a href=\"http://www.xe.com/iso4217.php\">official ISO 4217</a>
    currency codes are used, e.g.  `USD` or `EUR`.
    """

    eccn_ear99: Optional[str] = None
    r"""Export Control Classification Number, required on some exports from the United States."""

    metadata: Optional[str] = None
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """

    sku_code: Optional[str] = None
    r"""SKU code of the item, which is required by some carriers."""

    hs_code: Optional[str] = None
    r"""HS code of the item, which is required by some carriers. If `tariff_number` is not provided, `hs_code` will be used.  If both `hs_code` and `tariff_number` are provided, `tariff_number` will be used. 50 character limit."""

    tariff_number: Optional[str] = None
    r"""The tariff number of the item. If `tariff_number` is not provided, `hs_code` will be used. If both `hs_code` and `tariff_number` are provided, `tariff_number` will be used. 12 character limit."""

    object_created: Optional[datetime] = None
    r"""Date and time of object creation."""

    object_id: Optional[str] = None
    r"""Unique identifier of the given object."""

    object_owner: Optional[str] = None
    r"""Username of the user who created the object."""

    object_state: Optional[ObjectStateEnum] = None
    r"""Indicates the validity of the enclosing object"""

    object_updated: Optional[datetime] = None
    r"""Date and time of last object update."""

    test: Optional[bool] = None
    r"""Indicates whether the object has been created in test mode."""
