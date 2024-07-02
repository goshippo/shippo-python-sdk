"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from shippo.types import BaseModel
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class CustomsInvoicedChargesTypedDict(TypedDict):
    r"""Additional invoiced charges to be shown on the Customs Declaration Commercial Invoice."""
    
    currency: str
    r"""Currency for the invoiced charges amounts incurred on the end consumer."""
    total_shipping: NotRequired[str]
    r"""Total shipping paid by the buyer."""
    total_taxes: NotRequired[str]
    r"""Total taxes paid by the buyer."""
    total_duties: NotRequired[str]
    r"""Total duties paid by the buyer."""
    other_fees: NotRequired[str]
    r"""Other fees paid by the buyer."""
    

class CustomsInvoicedCharges(BaseModel):
    r"""Additional invoiced charges to be shown on the Customs Declaration Commercial Invoice."""
    
    currency: str
    r"""Currency for the invoiced charges amounts incurred on the end consumer."""
    total_shipping: Optional[str] = None
    r"""Total shipping paid by the buyer."""
    total_taxes: Optional[str] = None
    r"""Total taxes paid by the buyer."""
    total_duties: Optional[str] = None
    r"""Total duties paid by the buyer."""
    other_fees: Optional[str] = None
    r"""Other fees paid by the buyer."""
    
