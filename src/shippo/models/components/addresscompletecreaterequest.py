"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AddressCompleteCreateRequest:
    r"""Address represents the address as retrieved from the database"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""**required for purchase**<br>
    First and Last Name of the addressee
    """
    street1: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('street1') }})
    r"""**required for purchase**<br>
    First street line, 35 character limit. Usually street number and street name (except for DHL Germany, see street_no).
    """
    city: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('city') }})
    r"""**required for purchase**<br>
    Name of a city. When creating a Quote Address, sending a city is optional but will yield more accurate Rates. 
    Please bear in mind that city names may be ambiguous (there are 34 Springfields in the US). Pass in a state 
    or a ZIP code (see below), if known, it will yield more accurate results.
    """
    state: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('state') }})
    r"""**required for purchase for some countries**<br>
    State/Province values are required for shipments from/to the US, AU, and CA. UPS requires province for some 
    countries (i.e Ireland). To receive more accurate quotes, passing this field is recommended. Most carriers 
    only accept two or three character state abbreviations.
    """
    zip: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('zip') }})
    r"""**required for purchase**<br>
    Postal code of an Address. When creating a Quote Addresses, sending a ZIP is optional but will yield more 
    accurate Rates.
    """
    country: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('country') }})
    r"""Example: `US` or `DE`. All accepted values can be found on the
    <a href=\"http://www.iso.org/\" target=\"blank\">Official ISO Website</a>.
    Sending a country is always required.
    """
    company: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('company'), 'exclude': lambda f: f is None }})
    r"""Company Name"""
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
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    r"""Addresses containing a phone number allow carriers to call the recipient when delivering the Parcel. This
    increases the probability of delivery and helps to avoid accessorial charges after a Parcel has been shipped.
    """
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""E-mail address of the contact person, RFC3696/5321-compliant."""
    is_residential: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_residential'), 'exclude': lambda f: f is None }})
    metadata: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""A string of up to 100 characters that can be filled with any additional information you want
    to attach to the object.
    """
    latitude: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('latitude'), 'exclude': lambda f: f is None }})
    r"""Latitude of address"""
    longitude: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('longitude'), 'exclude': lambda f: f is None }})
    r"""Longitude of address"""
    validate: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validate'), 'exclude': lambda f: f is None }})
    

