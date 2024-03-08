"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomsInvoicedCharges:
    r"""Additional invoiced charges to be shown on the Customs Declaration Commercial Invoice."""
    currency: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency') }})
    r"""Currency for the invoiced charges amounts incurred on the end consumer."""
    total_shipping: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_shipping'), 'exclude': lambda f: f is None }})
    r"""Total shipping paid by the buyer."""
    total_taxes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_taxes'), 'exclude': lambda f: f is None }})
    r"""Total taxes paid by the buyer."""
    total_duties: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('total_duties'), 'exclude': lambda f: f is None }})
    r"""Total duties paid by the buyer."""
    other_fees: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('other_fees'), 'exclude': lambda f: f is None }})
    r"""Other fees paid by the buyer."""
    

