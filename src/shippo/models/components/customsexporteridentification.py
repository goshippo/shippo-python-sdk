"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .customstaxidentification import (
    CustomsTaxIdentification,
    CustomsTaxIdentificationTypedDict,
)
from shippo.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CustomsExporterIdentificationTypedDict(TypedDict):
    r"""Additional exporter identification that may be required to ship in certain countries"""

    eori_number: NotRequired[str]
    r"""Economic Operators' Registration and Identification (EORI) number. Must start with a 2 character
    country code followed by a 6-17 character alphanumeric identifier (e.g. PL1234567890ABCDE).
    <a href=\"https://ec.europa.eu/taxation_customs/business/customs-procedures/general-overview/economic-operators-registration-identification-number-eori_en\">More information on EORI.</a>
    """
    tax_id: NotRequired[CustomsTaxIdentificationTypedDict]
    r"""Tax identification that may be required to ship in certain countries. Typically used to assess duties on
    goods that are crossing a border.
    """


class CustomsExporterIdentification(BaseModel):
    r"""Additional exporter identification that may be required to ship in certain countries"""

    eori_number: Optional[str] = None
    r"""Economic Operators' Registration and Identification (EORI) number. Must start with a 2 character
    country code followed by a 6-17 character alphanumeric identifier (e.g. PL1234567890ABCDE).
    <a href=\"https://ec.europa.eu/taxation_customs/business/customs-procedures/general-overview/economic-operators-registration-identification-number-eori_en\">More information on EORI.</a>
    """

    tax_id: Optional[CustomsTaxIdentification] = None
    r"""Tax identification that may be required to ship in certain countries. Typically used to assess duties on
    goods that are crossing a border.
    """
