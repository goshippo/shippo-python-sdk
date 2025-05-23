"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .fedexconnectexistingownaccountparameters import (
    FedExConnectExistingOwnAccountParameters,
    FedExConnectExistingOwnAccountParametersTypedDict,
)
from .upsconnectexistingownaccountparameters import (
    UPSConnectExistingOwnAccountParameters,
    UPSConnectExistingOwnAccountParametersTypedDict,
)
from shippo.types import BaseModel
from typing import Any, Dict, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


ConnectExistingOwnAccountRequestParametersTypedDict = TypeAliasType(
    "ConnectExistingOwnAccountRequestParametersTypedDict",
    Union[
        FedExConnectExistingOwnAccountParametersTypedDict,
        UPSConnectExistingOwnAccountParametersTypedDict,
        Dict[str, Any],
    ],
)


ConnectExistingOwnAccountRequestParameters = TypeAliasType(
    "ConnectExistingOwnAccountRequestParameters",
    Union[
        FedExConnectExistingOwnAccountParameters,
        UPSConnectExistingOwnAccountParameters,
        Dict[str, Any],
    ],
)


class ConnectExistingOwnAccountRequestTypedDict(TypedDict):
    account_id: str
    carrier: str
    parameters: ConnectExistingOwnAccountRequestParametersTypedDict
    active: NotRequired[bool]
    metadata: NotRequired[str]
    test: NotRequired[bool]


class ConnectExistingOwnAccountRequest(BaseModel):
    account_id: str

    carrier: str

    parameters: ConnectExistingOwnAccountRequestParameters

    active: Optional[bool] = None

    metadata: Optional[str] = None

    test: Optional[bool] = None
