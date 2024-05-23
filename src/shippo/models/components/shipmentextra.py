"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .alcohol import Alcohol
from .billing import Billing
from .cod import Cod
from .customerreference import CustomerReference
from .dangerousgoodsobject import DangerousGoodsObject
from .departmentnumber import DepartmentNumber
from .dryice import DryIce
from .insurance import Insurance
from .invoicenumber import InvoiceNumber
from .ponumber import PoNumber
from .rmanumber import RmaNumber
from .upsreferencefields import UPSReferenceFields
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from shippo import utils
from typing import Optional


class AncillaryEndorsement(str, Enum):
    r"""Specify an ancillary service endorsement to provide the USPS with instructions on how to handle undeliverable-as-addressed pieces (DHL eCommerce only)."""
    FORWARDING_SERVICE_REQUESTED = 'FORWARDING_SERVICE_REQUESTED'
    RETURN_SERVICE_REQUESTED = 'RETURN_SERVICE_REQUESTED'


class DangerousGoodsCode(str, Enum):
    r"""Dangerous Goods Code (DHL eCommerce only). See <a href=\\"https://api-legacy.dhlecs.com/docs/v2/appendix.html#dangerous-goods\\">Category Codes</a>"""
    ONE = '01'
    TWO = '02'
    THREE = '03'
    FOUR = '04'
    FIVE = '05'
    SIX = '06'
    SEVEN = '07'
    EIGHT = '08'
    NINE = '09'


class LasershipAttrs(str, Enum):
    r"""Specify Lasership Attributes (Lasership only). Multiple options accepted."""
    TWO_PERSON_DELIVERY = 'TwoPersonDelivery'
    EXPLOSIVE = 'Explosive'
    ALCOHOL = 'Alcohol'
    HAZMAT = 'Hazmat'
    CONTROLLED_SUBSTANCE = 'ControlledSubstance'
    REFRIGERATED = 'Refrigerated'
    DRY_ICE = 'DryIce'
    PERISHABLE = 'Perishable'
    NO_RTS = 'NoRTS'


class PreferredDeliveryTimeframe(str, Enum):
    r"""Required for DHL Germany Paket Sameday. Designates a desired timeframe for delivery. Format is `HHMMHHMM`"""
    TEN_MILLION_ONE_THOUSAND_TWO_HUNDRED = '10001200'
    TWELVE_MILLION_ONE_THOUSAND_FOUR_HUNDRED = '12001400'
    FOURTEEN_MILLION_ONE_THOUSAND_SIX_HUNDRED = '14001600'
    SIXTEEN_MILLION_ONE_THOUSAND_EIGHT_HUNDRED = '16001800'
    EIGHTEEN_MILLION_TWO_THOUSAND = '18002000'
    NINETEEN_MILLION_TWO_THOUSAND_ONE_HUNDRED = '19002100'


class ReturnServiceType(str, Enum):
    r"""Request additional return option for return shipments (UPS only)."""
    PRINT_AND_MAIL = 'PRINT_AND_MAIL'
    ATTEMPT_1 = 'ATTEMPT_1'
    ATTEMPT_3 = 'ATTEMPT_3'
    ELECTRONIC_LABEL = 'ELECTRONIC_LABEL'


class SignatureConfirmation(str, Enum):
    r"""Request standard or adult signature confirmation. You can alternatively request Certified Mail (USPS only)
    or Indirect signature (FedEx only) or Carrier Confirmation (Deutsche Post only).
    """
    STANDARD = 'STANDARD'
    ADULT = 'ADULT'
    CERTIFIED = 'CERTIFIED'
    INDIRECT = 'INDIRECT'
    CARRIER_CONFIRMATION = 'CARRIER_CONFIRMATION'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ShipmentExtra:
    r"""An object holding optional extra services to be requested."""
    accounts_receivable_customer_account: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('accounts_receivable_customer_account'), 'exclude': lambda f: f is None }})
    alcohol: Optional[Alcohol] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alcohol'), 'exclude': lambda f: f is None }})
    r"""Indicates that a shipment contains Alcohol (Fedex and UPS only)."""
    ancillary_endorsement: Optional[AncillaryEndorsement] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ancillary_endorsement'), 'exclude': lambda f: f is None }})
    r"""Specify an ancillary service endorsement to provide the USPS with instructions on how to handle undeliverable-as-addressed pieces (DHL eCommerce only)."""
    appropriation_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('appropriation_number'), 'exclude': lambda f: f is None }})
    authority_to_leave: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authority_to_leave'), 'exclude': lambda f: f is None }})
    r"""Request `true` to give carrier permission to leave the parcel in a safe place if no one answers the
    door (where supported). When set to `false`, if no one is available to receive the item, the parcel 
    will not be left (*surcharges may be applicable).
    """
    bill_of_lading_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bill_of_lading_number'), 'exclude': lambda f: f is None }})
    billing: Optional[Billing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing'), 'exclude': lambda f: f is None }})
    r"""Specify billing details (UPS, FedEx, and DHL Germany only)."""
    bypass_address_validation: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bypass_address_validation'), 'exclude': lambda f: f is None }})
    r"""Bypasses address validation (USPS, UPS, & LaserShip only)."""
    carbon_neutral: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carbon_neutral'), 'exclude': lambda f: f is None }})
    r"""Request carbon offsets by passing true (UPS only)."""
    carrier_hub_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier_hub_id'), 'exclude': lambda f: f is None }})
    r"""Identifies the carrier injection site."""
    carrier_hub_travel_time: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('carrier_hub_travel_time'), 'exclude': lambda f: f is None }})
    r"""Travel time in hours from fulfillment center to carrier injection site."""
    cod: Optional[Cod] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('COD'), 'exclude': lambda f: f is None }})
    r"""Specify collection on delivery details (UPS only)."""
    cod_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cod_number'), 'exclude': lambda f: f is None }})
    container_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('container_type'), 'exclude': lambda f: f is None }})
    r"""Specify container type."""
    critical_pull_time: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('critical_pull_time'), 'exclude': lambda f: f is None }})
    r"""Carrier arrival time to pickup packages from the fulfillment center.
    UTC format: `%Y-%m-%dT%H:%M:%SZ`
    """
    customer_branch: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_branch'), 'exclude': lambda f: f is None }})
    r"""Specify customer branch (Lasership only)."""
    customer_reference: Optional[CustomerReference] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer_reference'), 'exclude': lambda f: f is None }})
    r"""Specify the reference field on the label (FedEx and UPS only)."""
    dangerous_goods: Optional[DangerousGoodsObject] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dangerous_goods'), 'exclude': lambda f: f is None }})
    r"""Container for specifying the presence of dangerous materials. This is specific to USPS, and if any contents
    are provided, only certain USPS service levels will be eligible. For more information, see our
    <a href=\"https://docs.goshippo.com/docs/shipments/hazmat/\">guide on hazardous or dangerous materials shipping</a>.
    """
    dangerous_goods_code: Optional[DangerousGoodsCode] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dangerous_goods_code'), 'exclude': lambda f: f is None }})
    r"""Dangerous Goods Code (DHL eCommerce only). See <a href=\\"https://api-legacy.dhlecs.com/docs/v2/appendix.html#dangerous-goods\\">Category Codes</a>"""
    dealer_order_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dealer_order_number'), 'exclude': lambda f: f is None }})
    delivery_instructions: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delivery_instructions'), 'exclude': lambda f: f is None }})
    r"""Specify delivery instructions. Up to 500 characters. (FedEx and OnTrac only)."""
    dept_number: Optional[DepartmentNumber] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dept_number'), 'exclude': lambda f: f is None }})
    r"""Specify the department number field on the label (FedEx and UPS only)."""
    dry_ice: Optional[DryIce] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dry_ice'), 'exclude': lambda f: f is None }})
    r"""Specify that the package contains Dry Ice (FedEx, Veho, and UPS only)."""
    fda_product_code: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fda_product_code'), 'exclude': lambda f: f is None }})
    fulfillment_center: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fulfillment_center'), 'exclude': lambda f: f is None }})
    r"""The fulfilment center where the package originates from."""
    insurance: Optional[Insurance] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insurance'), 'exclude': lambda f: f is None }})
    r"""To add 3rd party insurance powered by <a href=\\"https://docs.goshippo.com/docs/shipments/shippinginsurance/\\">XCover</a>, specify <br> `amount`, `content`, and `currency`. <br> Alternatively, you can choose carrier provided insurance by additionally specifying `provider` (UPS, FedEx and OnTrac only). <br><br> If you do not want to add insurance to you shipment, do not set these parameters."""
    invoice_number: Optional[InvoiceNumber] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('invoice_number'), 'exclude': lambda f: f is None }})
    r"""Specify the invoice number field on the label (FedEx and UPS only)."""
    is_return: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_return'), 'exclude': lambda f: f is None }})
    r"""This field specifies if it is a scan-based return shipment. See the <a href=\\"https://docs.goshippo.com/docs/shipments/returns/\\">Create a return shipment</a> section for more details."""
    lasership_attrs: Optional[LasershipAttrs] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lasership_attrs'), 'exclude': lambda f: f is None }})
    r"""Specify Lasership Attributes (Lasership only). Multiple options accepted."""
    lasership_declared_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lasership_declared_value'), 'exclude': lambda f: f is None }})
    r"""Declared value (Lasership only). Defaults to `50.00`."""
    manifest_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manifest_number'), 'exclude': lambda f: f is None }})
    model_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model_number'), 'exclude': lambda f: f is None }})
    part_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('part_number'), 'exclude': lambda f: f is None }})
    po_number: Optional[PoNumber] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('po_number'), 'exclude': lambda f: f is None }})
    r"""Specify the PO number field on the label (FedEx and UPS only)."""
    preferred_delivery_timeframe: Optional[PreferredDeliveryTimeframe] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferred_delivery_timeframe'), 'exclude': lambda f: f is None }})
    r"""Required for DHL Germany Paket Sameday. Designates a desired timeframe for delivery. Format is `HHMMHHMM`"""
    premium: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('premium'), 'exclude': lambda f: f is None }})
    r"""Add premium service to a shipment (DHL Germany international shipments only)."""
    production_code: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('production_code'), 'exclude': lambda f: f is None }})
    purchase_request_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('purchase_request_number'), 'exclude': lambda f: f is None }})
    qr_code_requested: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('qr_code_requested'), 'exclude': lambda f: f is None }})
    r"""Request a QR code for a given transaction when creating a shipping label (USPS domestic and Evri UK only)."""
    reference_1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference_1'), 'exclude': lambda f: f is None }})
    r"""Optional text to be printed on the shipping label if supported by carrier. Up to 50 characters."""
    reference_2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reference_2'), 'exclude': lambda f: f is None }})
    r"""Optional text to be printed on the shipping label if supported by carrier. Up to 50 characters. For DHL eCommerce, this field can be used for billing reference."""
    request_retail_rates: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('request_retail_rates'), 'exclude': lambda f: f is None }})
    r"""Returns retail rates instead of account-based rates (UPS and FedEx only)."""
    return_service_type: Optional[ReturnServiceType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('return_service_type'), 'exclude': lambda f: f is None }})
    r"""Request additional return option for return shipments (UPS only)."""
    rma_number: Optional[RmaNumber] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rma_number'), 'exclude': lambda f: f is None }})
    r"""Specify the RMA number field on the label (FedEx and UPS only)."""
    saturday_delivery: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('saturday_delivery'), 'exclude': lambda f: f is None }})
    r"""Marks shipment as to be delivered on a Saturday."""
    salesperson_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('salesperson_number'), 'exclude': lambda f: f is None }})
    serial_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serial_number'), 'exclude': lambda f: f is None }})
    signature_confirmation: Optional[SignatureConfirmation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('signature_confirmation'), 'exclude': lambda f: f is None }})
    r"""Request standard or adult signature confirmation. You can alternatively request Certified Mail (USPS only)
    or Indirect signature (FedEx only) or Carrier Confirmation (Deutsche Post only).
    """
    store_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('store_number'), 'exclude': lambda f: f is None }})
    transaction_reference_number: Optional[UPSReferenceFields] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transaction_reference_number'), 'exclude': lambda f: f is None }})
    

