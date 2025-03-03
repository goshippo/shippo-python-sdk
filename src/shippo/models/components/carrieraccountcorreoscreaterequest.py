"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Final


@dataclasses.dataclass
class CarrierAccountCorreosCreateRequestParameters:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CarrierAccountCorreosCreateRequest:
    parameters: CarrierAccountCorreosCreateRequestParameters = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters') }})
    CARRIER: Final[str] = dataclasses.field(default='correos', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier') }})
    

