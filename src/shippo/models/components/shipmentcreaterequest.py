"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addresscreaterequest import AddressCreateRequest
from .customsdeclarationcreaterequest import CustomsDeclarationCreateRequest
from .parcelcreatefromtemplaterequest import ParcelCreateFromTemplateRequest
from .parcelcreaterequest import ParcelCreateRequest
from .shipmentextra import ShipmentExtra
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShipmentCreateRequest:
    address_from: ShipmentCreateRequestAddressFrom = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_from') }})
    address_to: ShipmentCreateRequestAddressTo = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_to') }})
    parcels: List[Parcels] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parcels') }})
    extra: Optional[ShipmentExtra] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extra'), 'exclude': lambda f: f is None }})
    r"""An object holding optional extra services to be requested."""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want to attach to the object."""
    shipment_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shipment_date'), 'exclude': lambda f: f is None }})
    r"""Date the shipment will be tendered to the carrier. Must be in the format `2014-01-18T00:35:03.463Z`.
    Defaults to current date and time if no value is provided. Please note that some carriers require this value to
    be in the future, on a working day, or similar.
    """
    address_return: Optional[AddressReturn] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_return'), 'exclude': lambda f: f is None }})
    customs_declaration: Optional[ShipmentCreateRequestCustomsDeclaration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customs_declaration'), 'exclude': lambda f: f is None }})
    async_: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('async'), 'exclude': lambda f: f is None }})
    carrier_accounts: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier_accounts'), 'exclude': lambda f: f is None }})
    r"""List of <a href=\\"#tag/Carrier-Accounts/\\">Carrier Accounts</a> `object_id`s used to filter
    the returned rates.  If set, only rates from these carriers will be returned.
    """
    


ShipmentCreateRequestAddressFrom = Union[AddressCreateRequest, str]

AddressReturn = Union[AddressCreateRequest, str]

ShipmentCreateRequestAddressTo = Union[AddressCreateRequest, str]

ShipmentCreateRequestCustomsDeclaration = Union[CustomsDeclarationCreateRequest, str]

Parcels = Union[ParcelCreateRequest, ParcelCreateFromTemplateRequest, str]
