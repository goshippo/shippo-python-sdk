"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Final


@dataclasses.dataclass
class CarrierAccountDeutschePostCreateRequestParameters:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CarrierAccountDeutschePostCreateRequest:
    parameters: CarrierAccountDeutschePostCreateRequestParameters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    CARRIER: Final[str] = dataclasses.field(default='deutsche_post', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier') }})
    

