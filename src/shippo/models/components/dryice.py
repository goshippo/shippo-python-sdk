"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DryIceTypedDict(TypedDict):
    r"""Specify that the package contains Dry Ice (FedEx, Veho, and UPS only)."""

    contains_dry_ice: NotRequired[bool]
    r"""Mandatory. Specifies that the package contains Dry Ice."""
    weight: NotRequired[str]
    r"""Mandatory. Units must be in Kilograms. Cannot be greater than package weight."""


class DryIce(BaseModel):
    r"""Specify that the package contains Dry Ice (FedEx, Veho, and UPS only)."""

    contains_dry_ice: Optional[bool] = None
    r"""Mandatory. Specifies that the package contains Dry Ice."""

    weight: Optional[str] = None
    r"""Mandatory. Units must be in Kilograms. Cannot be greater than package weight."""
