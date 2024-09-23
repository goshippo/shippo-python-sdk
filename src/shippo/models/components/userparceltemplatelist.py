"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .userparceltemplate import UserParcelTemplate
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserParcelTemplateList:
    results: Optional[List[UserParcelTemplate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    

