"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .carrieraccountdhlexpresscreaterequestparameters import CarrierAccountDHLExpressCreateRequestParameters, CarrierAccountDHLExpressCreateRequestParametersTypedDict
from shippo.types import BaseModel
from typing import TypedDict


class CarrierAccountDHLExpressCreateRequestTypedDict(TypedDict):
    carrier: str
    parameters: CarrierAccountDHLExpressCreateRequestParametersTypedDict
    

class CarrierAccountDHLExpressCreateRequest(BaseModel):
    carrier: str
    parameters: CarrierAccountDHLExpressCreateRequestParameters
    
