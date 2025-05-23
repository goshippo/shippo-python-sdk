"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .weightunitenum import WeightUnitEnum
from datetime import datetime
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class LineItemBaseTypedDict(TypedDict):
    currency: NotRequired[str]
    r"""Currency of the <code>total_price</code> amount."""
    manufacture_country: NotRequired[str]
    r"""Country the item was manufactured in. In the Shippo dashboard, this value will be used ot pre-fill the customs declaration when creating a label for this order."""
    max_delivery_time: NotRequired[datetime]
    r"""The date and time this item needs to be delivered by, i.e. by when the carrier delivers it to the buyer.
    This value is used by some platforms such as eBay to measure a seller's shipping time and performance.
    It will be displayed in the Shippo dashboard.
    """
    max_ship_time: NotRequired[datetime]
    r"""The date and time this item needs to be fulfilled by, i.e. by when the shipping label needs to be
    created and handed over to the carrier. This value is used by some platforms such as eBay to measure
    a seller's handling time and performance. It will be displayed in the Shippo dashboard.
    """
    quantity: NotRequired[int]
    r"""The quantity of this item in this order."""
    sku: NotRequired[str]
    r"""The stock keeping unit value of this item."""
    title: NotRequired[str]
    r"""Title of the line item."""
    total_price: NotRequired[str]
    r"""Total price paid by the buyer for this item (or these items, if quantity > 1)."""
    variant_title: NotRequired[str]
    r"""A variant is a specific variation of an item (e.g. `size M` or `color blue`).
    Variants might be exposed as a separate resource in the future too.
    Currently the variant title is a free text field describing the variant.
    """
    weight: NotRequired[str]
    r"""Total weight of this/these item(s). Instead of specifying the weight of all items,
    you can also set the <code>total_weight</code> value of the order object.
    """
    weight_unit: NotRequired[WeightUnitEnum]
    r"""The unit used for weight."""


class LineItemBase(BaseModel):
    currency: Optional[str] = None
    r"""Currency of the <code>total_price</code> amount."""

    manufacture_country: Optional[str] = None
    r"""Country the item was manufactured in. In the Shippo dashboard, this value will be used ot pre-fill the customs declaration when creating a label for this order."""

    max_delivery_time: Optional[datetime] = None
    r"""The date and time this item needs to be delivered by, i.e. by when the carrier delivers it to the buyer.
    This value is used by some platforms such as eBay to measure a seller's shipping time and performance.
    It will be displayed in the Shippo dashboard.
    """

    max_ship_time: Optional[datetime] = None
    r"""The date and time this item needs to be fulfilled by, i.e. by when the shipping label needs to be
    created and handed over to the carrier. This value is used by some platforms such as eBay to measure
    a seller's handling time and performance. It will be displayed in the Shippo dashboard.
    """

    quantity: Optional[int] = None
    r"""The quantity of this item in this order."""

    sku: Optional[str] = None
    r"""The stock keeping unit value of this item."""

    title: Optional[str] = None
    r"""Title of the line item."""

    total_price: Optional[str] = None
    r"""Total price paid by the buyer for this item (or these items, if quantity > 1)."""

    variant_title: Optional[str] = None
    r"""A variant is a specific variation of an item (e.g. `size M` or `color blue`).
    Variants might be exposed as a separate resource in the future too.
    Currently the variant title is a free text field describing the variant.
    """

    weight: Optional[str] = None
    r"""Total weight of this/these item(s). Instead of specifying the weight of all items,
    you can also set the <code>total_weight</code> value of the order object.
    """

    weight_unit: Optional[WeightUnitEnum] = None
    r"""The unit used for weight."""
