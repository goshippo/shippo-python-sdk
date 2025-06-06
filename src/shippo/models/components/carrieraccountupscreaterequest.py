"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .carrieraccountupscreaterequestparameters import (
    CarrierAccountUPSCreateRequestParameters,
    CarrierAccountUPSCreateRequestParametersTypedDict,
)
import pydantic
from pydantic.functional_validators import AfterValidator
from shippo.types import BaseModel
from shippo.utils import validate_const
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CarrierAccountUPSCreateRequestTypedDict(TypedDict):
    carrier: Literal["ups"]
    parameters: NotRequired[CarrierAccountUPSCreateRequestParametersTypedDict]


class CarrierAccountUPSCreateRequest(BaseModel):
    CARRIER: Annotated[
        Annotated[Literal["ups"], AfterValidator(validate_const("ups"))],
        pydantic.Field(alias="carrier"),
    ] = "ups"

    parameters: Optional[CarrierAccountUPSCreateRequestParameters] = None
