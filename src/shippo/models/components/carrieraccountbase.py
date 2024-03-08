"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Any, Dict, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CarrierAccountBase:
    account_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account_id') }})
    r"""Unique identifier of the account. Please check the <a href=\\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\\">carrier accounts tutorial</a>
    page for the `account_id` per carrier.<br> 
    To protect account information, this field will be masked in any API response.
    """
    carrier: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier') }})
    r"""Carrier token, see <a href=\\"#tag/Carriers\\">Carriers</a><br>
    Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a> page for all supported carriers.
    """
    active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('active'), 'exclude': lambda f: f is None }})
    r"""Determines whether the account is active. When creating a shipment, if no `carrier_accounts` are explicitly
    passed Shippo will query all carrier accounts that have this field set. By default, this is set to True.
    """
    parameters: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parameters'), 'exclude': lambda f: f is None }})
    r"""An array of additional parameters for the account, such as e.g. password or token.
    Please check the <a href=\"https://docs.goshippo.com/docs/carriers/carrieraccounts/\">carrier accounts tutorial</a> page for the parameters per carrier.<br> 
    To protect account information, this field will be masked in any API response.
    """
    

