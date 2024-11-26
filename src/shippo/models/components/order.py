"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .address import Address
from .lineitem import LineItem
from .ordershopappenum import OrderShopAppEnum
from .orderstatusenum import OrderStatusEnum
from .weightunitenum import WeightUnitEnum
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import List, Optional


@dataclasses.dataclass
class Transactions:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Order:
    placed_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('placed_at') }})
    r"""Date and time when the order was placed. This datetime can be different from the datetime of the order object creation on Shippo."""
    to_address: Address = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('to_address') }})
    r"""<a href=\\"#tag/Addresses\\">Address</a> object of the recipient / buyer. Will be returned expanded by default."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""**Required if total_price is provided**<br>
    Currency of the <code>total_price</code> and <code>total_tax</code> amounts.
    """
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Custom buyer- or seller-provided notes about the order."""
    order_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_number'), 'exclude': lambda f: f is None }})
    r"""An alphanumeric identifier for the order used by the seller/buyer. This identifier doesn't need to be unique."""
    order_status: Optional[OrderStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order_status'), 'exclude': lambda f: f is None }})
    r"""Current state of the order. See the <a href=\\"https://docs.goshippo.com/docs/orders/orders/\\">orders tutorial</a>
    for the logic of how the status is handled.
    """
    shipping_cost: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_cost'), 'exclude': lambda f: f is None }})
    r"""Amount paid by the buyer for shipping. This amount can be different from the price the seller will actually pay for shipping."""
    shipping_cost_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_cost_currency'), 'exclude': lambda f: f is None }})
    r"""**Required if shipping_cost is provided**<br>
    Currency of the <code>shipping_cost</code> amount.
    """
    shipping_method: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipping_method'), 'exclude': lambda f: f is None }})
    r"""Shipping method (carrier + service or other free text description) chosen by the buyer.
    This value can be different from the shipping method the seller will actually choose.
    """
    subtotal_price: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subtotal_price'), 'exclude': lambda f: f is None }})
    total_price: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_price'), 'exclude': lambda f: f is None }})
    r"""Total amount paid by the buyer for this order."""
    total_tax: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_tax'), 'exclude': lambda f: f is None }})
    r"""Total tax amount paid by the buyer for this order."""
    weight: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight'), 'exclude': lambda f: f is None }})
    r"""Total weight of the order."""
    weight_unit: Optional[WeightUnitEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weight_unit'), 'exclude': lambda f: f is None }})
    r"""The unit used for weight."""
    from_address: Optional[Address] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('from_address'), 'exclude': lambda f: f is None }})
    r"""<a href=\\"#tag/Addresses\\">Address</a> object of the sender / seller. Will be returned expanded by default."""
    line_items: Optional[List[LineItem]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('line_items'), 'exclude': lambda f: f is None }})
    r"""Array of <a href=\\"#section/Line-Item\\">line item</a> objects representing the items in this order.
    All objects will be returned expanded by default.
    """
    object_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id'), 'exclude': lambda f: f is None }})
    r"""Unique identifier of the order object."""
    object_owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_owner'), 'exclude': lambda f: f is None }})
    r"""Username of the user who created the object."""
    shop_app: Optional[OrderShopAppEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shop_app'), 'exclude': lambda f: f is None }})
    r"""Platform the order was created on and, if applicable, imported from.
    Orders created via the Shippo API or dashboard will have the value \"Shippo\".
    """
    transactions: Optional[List[Transactions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transactions'), 'exclude': lambda f: f is None }})
    r"""Array of <a href=\\"#tag/Transactions\\">transaction</a> objects representing all shipping labels purchased for this order.
    All objects are returned expanded with a limited number of fields by default.
    """
    

