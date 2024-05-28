"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ParentServicelevel:
    r"""Used for some Service Levels to link to the more \\"generic\\" version of this Service Level - for example,
    if this Service Level is a variation specific to shipments to Europe(\"ups_saver_eu\"), the \"parent\" is 
    the fully generic version (\"ups_saver\"). Helpful when displaying Service Levels to users. Has the same 
    structure of the servicelevel - \"name\", \"token\", \"terms\", and \"extended_token\", or it is otherwise null.
    """
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the Rate's servicelevel, e.g. `International Priority` or `Standard Post`.
    A servicelevel commonly defines the transit time of a Shipment (e.g., Express vs. Standard), along with other properties. 
    These names vary depending on the provider.
    """
    terms: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terms'), 'exclude': lambda f: f is None }})
    r"""Further clarification of the service."""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Token of the Rate's servicelevel, e.g. `usps_priority` or `fedex_ground`.
    See <a href=\"#tag/Service-Levels\">servicelevels</a>.
    """
    extended_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extended_token'), 'exclude': lambda f: f is None }})
    r"""Unique, extended version of the Service Level \\"token\\".
    Guaranteed to be unique across all Service Levels, and may help offer insight into the specific Service Level it describes.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ServiceLevelWithParent:
    r"""Contains details regarding the service level for the given rate."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the Rate's servicelevel, e.g. `International Priority` or `Standard Post`.
    A servicelevel commonly defines the transit time of a Shipment (e.g., Express vs. Standard), along with other properties. 
    These names vary depending on the provider.
    """
    terms: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('terms'), 'exclude': lambda f: f is None }})
    r"""Further clarification of the service."""
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    r"""Token of the Rate's servicelevel, e.g. `usps_priority` or `fedex_ground`.
    See <a href=\"#tag/Service-Levels\">servicelevels</a>.
    """
    extended_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extended_token'), 'exclude': lambda f: f is None }})
    r"""Unique, extended version of the Service Level \\"token\\".
    Guaranteed to be unique across all Service Levels, and may help offer insight into the specific Service Level it describes.
    """
    parent_servicelevel: Optional[ParentServicelevel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent_servicelevel'), 'exclude': lambda f: f is None }})
    
