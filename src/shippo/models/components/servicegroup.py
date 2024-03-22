"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .servicegrouptype import ServiceGroupType
from .servicelevel import ServiceLevel
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServiceGroup:
    description: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description') }})
    r"""Description for the service group"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Name for the service group that will be shown to customers in the response"""
    type: ServiceGroupType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of the service group.<br> `LIVE_RATE` - Shippo will make a rating request and return real-time rates for the shipping group, only falling back to the specified flat rate amount if no rates match a service level in the service group.<br> `FLAT_RATE` - Returns a shipping option with the specified flat rate amount.<br> `FREE_SHIPPING` - Returns a shipping option with a price of $0 only if the total cost of items exceeds the amount defined by `free_shipping_threshold_min`"""
    object_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id') }})
    r"""The unique identifier of the given Service Group object."""
    service_levels: List[ServiceLevel] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_levels') }})
    flat_rate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flat_rate'), 'exclude': lambda f: f is None }})
    r"""String representation of an amount to be returned as the flat rate
    if 1. The service group is of type `LIVE_RATE` and no matching rates
    were found; or 2. The service group is of type `FLAT_RATE`. Either
    integers or decimals are accepted. Required unless type is
    `FREE_SHIPPING`
    """
    flat_rate_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('flat_rate_currency'), 'exclude': lambda f: f is None }})
    r"""required unless type is `FREE_SHIPPING`. (ISO 4217 currency)"""
    free_shipping_threshold_currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('free_shipping_threshold_currency'), 'exclude': lambda f: f is None }})
    r"""optional unless type is `FREE_SHIPPING`. (ISO 4217 currency)"""
    free_shipping_threshold_min: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('free_shipping_threshold_min'), 'exclude': lambda f: f is None }})
    r"""For service groups of type `FREE_SHIPPING`, this field must be required to configure the minimum cart total (total cost of items in the cart) for this service group to be returned for rates at checkout. Optional unless type is `FREE_SHIPPING`"""
    rate_adjustment: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rate_adjustment'), 'exclude': lambda f: f is None }})
    r"""The amount in percent (%) that the service group's returned rate should be adjusted. For example, if this field is set to 5 and the matched rate price is $5.00, the returned value of the service group will be $5.25. Negative integers are also accepted and will discount the rate price by the defined percentage amount."""
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    r"""True if the service group is enabled, false otherwise."""
    

