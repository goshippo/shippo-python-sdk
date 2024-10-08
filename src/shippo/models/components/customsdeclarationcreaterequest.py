"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addressimporter import AddressImporter
from .customsdeclarationb13afilingoptionenum import CustomsDeclarationB13AFilingOptionEnum
from .customsdeclarationcontentstypeenum import CustomsDeclarationContentsTypeEnum
from .customsdeclarationeelpfcenum import CustomsDeclarationEelPfcEnum
from .customsdeclarationincotermenum import CustomsDeclarationIncotermEnum
from .customsdeclarationnondeliveryoptionenum import CustomsDeclarationNonDeliveryOptionEnum
from .customsexporteridentification import CustomsExporterIdentification
from .customsitemcreaterequest import CustomsItemCreateRequest
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import List, Optional


class CustomsDeclarationCreateRequestType(str, Enum):
    r"""Party to be billed for duties."""
    SENDER = 'SENDER'
    RECIPIENT = 'RECIPIENT'
    THIRD_PARTY = 'THIRD_PARTY'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomsDeclarationCreateRequestAddress:
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the party to be billed for duties."""
    zip: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip'), 'exclude': lambda f: f is None }})
    r"""Postal code of the party to be billed for duties."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Country ISO code of account number to be billed."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DutiesPayor:
    r"""Specifies who will pay the duties for the shipment. Only accepted for FedEx shipments."""
    account: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('account'), 'exclude': lambda f: f is None }})
    r"""Account number to be billed for duties."""
    type: Optional[CustomsDeclarationCreateRequestType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    r"""Party to be billed for duties."""
    address: Optional[CustomsDeclarationCreateRequestAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomsDeclarationCreateRequest:
    certify: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify') }})
    r"""Expresses that the certify_signer has provided all information of this customs declaration truthfully."""
    certify_signer: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certify_signer') }})
    r"""Name of the person who created the customs declaration and is responsible for the validity of all
    information provided.
    """
    contents_type: CustomsDeclarationContentsTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contents_type') }})
    items: List[CustomsItemCreateRequest] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    non_delivery_option: CustomsDeclarationNonDeliveryOptionEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('non_delivery_option') }})
    aes_itn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('aes_itn'), 'exclude': lambda f: f is None }})
    r"""**required if eel_pfc is `AES_ITN`**<br>
    AES / ITN reference of the shipment.
    """
    b13a_filing_option: Optional[CustomsDeclarationB13AFilingOptionEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('b13a_filing_option'), 'exclude': lambda f: f is None }})
    b13a_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('b13a_number'), 'exclude': lambda f: f is None }})
    r"""**must be provided if and only if b13a_filing_option is provided**<br>
    Represents:<br> the Proof of Report (POR) Number when b13a_filing_option is `FILED_ELECTRONICALLY`;<br> 
    the Summary ID Number when b13a_filing_option is `SUMMARY_REPORTING`;<br> 
    or the Exemption Number when b13a_filing_option is `NOT_REQUIRED`.
    """
    certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('certificate'), 'exclude': lambda f: f is None }})
    r"""Certificate reference of the shipment."""
    commercial_invoice: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commercial_invoice'), 'exclude': lambda f: f is None }})
    contents_explanation: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contents_explanation'), 'exclude': lambda f: f is None }})
    r"""**required if contents_type is `OTHER`**<br>
    Explanation of the type of goods of the shipment.
    """
    disclaimer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disclaimer'), 'exclude': lambda f: f is None }})
    r"""Disclaimer for the shipment and customs information that have been provided."""
    duties_payor: Optional[DutiesPayor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duties_payor'), 'exclude': lambda f: f is None }})
    r"""Specifies who will pay the duties for the shipment. Only accepted for FedEx shipments."""
    exporter_identification: Optional[CustomsExporterIdentification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exporter_identification'), 'exclude': lambda f: f is None }})
    r"""Additional exporter identification that may be required to ship in certain countries"""
    exporter_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('exporter_reference'), 'exclude': lambda f: f is None }})
    r"""Exporter reference of an export shipment."""
    importer_reference: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('importer_reference'), 'exclude': lambda f: f is None }})
    r"""Importer reference of an import shipment."""
    is_vat_collected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_vat_collected'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the shipment's destination VAT has been collected. May be required for some destinations."""
    invoice: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice'), 'exclude': lambda f: f is None }})
    r"""Invoice reference of the shipment."""
    license: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('license'), 'exclude': lambda f: f is None }})
    r"""License reference of the shipment."""
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you
    want to attach to the object.
    """
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Additional notes to be included in the customs declaration."""
    address_importer: Optional[AddressImporter] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address_importer'), 'exclude': lambda f: f is None }})
    r"""Object that represents the address of the importer"""
    eel_pfc: Optional[CustomsDeclarationEelPfcEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eel_pfc'), 'exclude': lambda f: f is None }})
    incoterm: Optional[CustomsDeclarationIncotermEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('incoterm'), 'exclude': lambda f: f is None }})
    test: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('test'), 'exclude': lambda f: f is None }})
    

