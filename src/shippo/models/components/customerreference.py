"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomerReference:
    r"""Specify the reference field on the label (FedEx and UPS only)."""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""Custom prefix for customer reference field (ZPL labels only). Up to 11 characters, including trailing
    spaces. Empty string indicates removal of default prefix. To use the default prefix, do not include
    this property.
    """
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    r"""Optional text to be printed on the shipping label for customer reference. Up to 40 characters. If
    this is provided, reference_1 will be ignored.
    """
    ref_sort: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ref_sort'), 'exclude': lambda f: f is None }})
    r"""Order UPS reference fields are printed on ZPL labels. For UPS shipments, if you choose to set `ref_sort` for one reference, you must set `ref_sort` for all other supported UPS references using unique integers."""
    

