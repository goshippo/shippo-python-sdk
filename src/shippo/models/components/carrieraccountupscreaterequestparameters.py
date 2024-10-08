"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CarrierAccountUPSCreateRequestParameters:
    billing_address_city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_city') }})
    billing_address_country_iso2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_country_iso2') }})
    billing_address_state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_state') }})
    billing_address_street1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_street1') }})
    billing_address_zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_zip') }})
    pickup_address_city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_city') }})
    r"""User's pickup address city."""
    pickup_address_country_iso2: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_country_iso2') }})
    r"""User's pickup street 1."""
    pickup_address_state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_state') }})
    r"""User's pickup address state."""
    pickup_address_street1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_street1') }})
    r"""User's pickup address street 1."""
    pickup_address_zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_zip') }})
    r"""User's pickup address zip code."""
    ups_agreements: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ups_agreements') }})
    r"""Whether the user agrees to the UPS terms and conditions or not. Error 400 will be returned if passed in as false"""
    billing_address_street2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address_street2'), 'exclude': lambda f: f is None }})
    r"""Empty string acceptable for billing_address_street2"""
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""Company name. Full name is acceptable in this field if the user has no company name"""
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    full_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_name'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Needs to be a valid phone number and cannot be null"""
    pickup_address_same_as_billing_address: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_same_as_billing_address'), 'exclude': lambda f: f is None }})
    pickup_address_street2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pickup_address_street2'), 'exclude': lambda f: f is None }})
    r"""User's pickup street 2."""
    

