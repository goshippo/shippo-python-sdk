"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from .fedexconnectexistingownaccountparameters import FedExConnectExistingOwnAccountParameters, FedExConnectExistingOwnAccountParametersTypedDict
from .upsconnectexistingownaccountparameters import UPSConnectExistingOwnAccountParameters, UPSConnectExistingOwnAccountParametersTypedDict
from shippo.types import BaseModel
from typing import Any, Dict, Optional, TypedDict, Union
from typing_extensions import NotRequired


class CarrierAccountBaseTypedDict(TypedDict):
    account_id: str
    r"""Unique identifier of the account. Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a>
    page for the `account_id` per carrier.<br>
    To protect account information, this field will be masked in any API response.
    """
    carrier: str
    r"""Carrier token, see <a href=\"#tag/Carriers\">Carriers</a><br>
    Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a> page for all supported carriers.
    """
    active: NotRequired[bool]
    r"""Determines whether the account is active. When creating a shipment, if no `carrier_accounts` are explicitly
    passed Shippo will query all carrier accounts that have this field set. By default, this is set to True.
    """
    parameters: NotRequired[CarrierAccountBaseParametersTypedDict]
    

class CarrierAccountBase(BaseModel):
    account_id: str
    r"""Unique identifier of the account. Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a>
    page for the `account_id` per carrier.<br>
    To protect account information, this field will be masked in any API response.
    """
    carrier: str
    r"""Carrier token, see <a href=\"#tag/Carriers\">Carriers</a><br>
    Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a> page for all supported carriers.
    """
    active: Optional[bool] = None
    r"""Determines whether the account is active. When creating a shipment, if no `carrier_accounts` are explicitly
    passed Shippo will query all carrier accounts that have this field set. By default, this is set to True.
    """
    parameters: Optional[CarrierAccountBaseParameters] = None
    

CarrierAccountBaseParametersTypedDict = Union[FedExConnectExistingOwnAccountParametersTypedDict, UPSConnectExistingOwnAccountParametersTypedDict, Dict[str, Any]]


CarrierAccountBaseParameters = Union[FedExConnectExistingOwnAccountParameters, UPSConnectExistingOwnAccountParameters, Dict[str, Any]]

