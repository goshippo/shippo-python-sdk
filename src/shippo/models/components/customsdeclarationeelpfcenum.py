"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class CustomsDeclarationEelPfcEnum(str, Enum):
    r"""EEL / PFC type of the shipment. For most shipments from the US to CA, `NOEEI_30_36` is applicable; for most
    other shipments from the US, `NOEEI_30_37_a` is applicable.
    """
    NOEEI_30_37_A = 'NOEEI_30_37_a'
    NOEEI_30_37_H = 'NOEEI_30_37_h'
    NOEEI_30_37_F = 'NOEEI_30_37_f'
    NOEEI_30_36 = 'NOEEI_30_36'
    AES_ITN = 'AES_ITN'
