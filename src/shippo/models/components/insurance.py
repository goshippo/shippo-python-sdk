"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional


class Provider(str, Enum):
    r"""To have insurance cover provided by a carrier directly instead of Shippo's provider (XCover), set `provider` to `FEDEX`, `UPS`, or `ONTRAC`."""
    FEDEX = 'FEDEX'
    UPS = 'UPS'
    ONTRAC = 'ONTRAC'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Insurance:
    r"""To add 3rd party insurance powered by <a href=\\"https://docs.goshippo.com/docs/shipments/shippinginsurance/\\">XCover</a>,
    specify <br> `amount`, `content`, and `currency`. <br> Alternatively, you can choose carrier provided insurance 
    by additionally specifying `provider` (UPS, FedEx and OnTrac only). <br><br> If you do not want to add insurance 
    to your shipment, do not set these parameters.
    """
    amount: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount'), 'exclude': lambda f: f is None }})
    r"""Declared value of the goods you want to insure."""
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('content'), 'exclude': lambda f: f is None }})
    r"""Description of package content."""
    currency: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency'), 'exclude': lambda f: f is None }})
    r"""Currency for the amount value.
    Currently only USD is supported for FedEx and UPS.
    """
    provider: Optional[Provider] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provider'), 'exclude': lambda f: f is None }})
    r"""To have insurance cover provided by a carrier directly instead of Shippo's provider (XCover), set `provider` to `FEDEX`, `UPS`, or `ONTRAC`."""
    

