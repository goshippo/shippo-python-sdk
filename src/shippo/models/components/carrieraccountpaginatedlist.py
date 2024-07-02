"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .carrieraccountwithextrainfo import CarrierAccountWithExtraInfo, CarrierAccountWithExtraInfoTypedDict
from shippo.types import BaseModel
from typing import List, Optional, TypedDict
from typing_extensions import NotRequired


class CarrierAccountPaginatedListTypedDict(TypedDict):
    next: NotRequired[str]
    previous: NotRequired[str]
    results: NotRequired[List[CarrierAccountWithExtraInfoTypedDict]]
    

class CarrierAccountPaginatedList(BaseModel):
    next: Optional[str] = None
    previous: Optional[str] = None
    results: Optional[List[CarrierAccountWithExtraInfo]] = None
    
