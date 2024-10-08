"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddressImporter:
    r"""Object that represents the address of the importer"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""First and Last Name of the addressee"""
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""Company Name"""
    street1: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street1'), 'exclude': lambda f: f is None }})
    r"""First street line, 35 character limit. Usually street number and street name (except for DHL Germany, see street_no)."""
    street2: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street2'), 'exclude': lambda f: f is None }})
    r"""Second street line, 35 character limit."""
    street3: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street3'), 'exclude': lambda f: f is None }})
    r"""Third street line, 35 character limit.
    Only accepted for USPS international shipments, UPS domestic and UPS international shipments.
    """
    street_no: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street_no'), 'exclude': lambda f: f is None }})
    r"""Street number of the addressed building.
    This field can be included in street1 for all carriers except for DHL Germany.
    """
    city: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city'), 'exclude': lambda f: f is None }})
    r"""Name of a city"""
    state: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state'), 'exclude': lambda f: f is None }})
    r"""**required for purchase for some countries**<br>
    State/Province values are required for shipments from/to the US, AU, and CA. UPS requires province for some 
    countries (i.e Ireland). To receive more accurate quotes, passing this field is recommended. Most carriers 
    only accept two or three character state abbreviations.
    """
    zip: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip'), 'exclude': lambda f: f is None }})
    r"""Postal code of an Address."""
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country'), 'exclude': lambda f: f is None }})
    r"""Example: `US` or `DE`. All accepted values can be found on the
    <a href=\"http://www.iso.org/\" target=\"blank\">Official ISO Website</a>.
    Sending a country is always required.
    """
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Addresses containing a phone number allow carriers to call the recipient when delivering the Parcel. This
    increases the probability of delivery and helps to avoid accessorial charges after a Parcel has been shipped.
    """
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""E-mail address of the contact person, RFC3696/5321-compliant."""
    is_residential: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_residential'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the address provided is a residential address or not."""
    

