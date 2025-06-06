"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from pydantic import Discriminator, Tag
from shippo.models.components import (
    carrieraccountcanadapostcreaterequest as components_carrieraccountcanadapostcreaterequest,
    carrieraccountchronopostcreaterequest as components_carrieraccountchronopostcreaterequest,
    carrieraccountcolissimocreaterequest as components_carrieraccountcolissimocreaterequest,
    carrieraccountcorreoscreaterequest as components_carrieraccountcorreoscreaterequest,
    carrieraccountdeutschepostcreaterequest as components_carrieraccountdeutschepostcreaterequest,
    carrieraccountdhlexpresscreaterequest as components_carrieraccountdhlexpresscreaterequest,
    carrieraccountdpddecreaterequest as components_carrieraccountdpddecreaterequest,
    carrieraccountdpdukcreaterequest as components_carrieraccountdpdukcreaterequest,
    carrieraccountfedexcreaterequest as components_carrieraccountfedexcreaterequest,
    carrieraccounthermesukcreaterequest as components_carrieraccounthermesukcreaterequest,
    carrieraccountmondialrelaycreaterequest as components_carrieraccountmondialrelaycreaterequest,
    carrieraccountposteitalianecreaterequest as components_carrieraccountposteitalianecreaterequest,
    carrieraccountsendlecreaterequest as components_carrieraccountsendlecreaterequest,
    carrieraccountupscreaterequest as components_carrieraccountupscreaterequest,
    carrieraccountuspscreaterequest as components_carrieraccountuspscreaterequest,
)
from shippo.types import BaseModel
from shippo.utils import FieldMetadata, HeaderMetadata, get_discriminator
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class RegisterCarrierAccountGlobalsTypedDict(TypedDict):
    shippo_api_version: NotRequired[str]
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


class RegisterCarrierAccountGlobals(BaseModel):
    shippo_api_version: Annotated[
        Optional[str],
        pydantic.Field(alias="SHIPPO-API-VERSION"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional string used to pick a non-default API version to use. See our <a href=\"https://docs.goshippo.com/docs/api_concepts/apiversioning/\">API version</a> guide."""


RegisterCarrierAccountRequestTypedDict = TypeAliasType(
    "RegisterCarrierAccountRequestTypedDict",
    Union[
        components_carrieraccountcanadapostcreaterequest.CarrierAccountCanadaPostCreateRequestTypedDict,
        components_carrieraccountchronopostcreaterequest.CarrierAccountChronopostCreateRequestTypedDict,
        components_carrieraccountcolissimocreaterequest.CarrierAccountColissimoCreateRequestTypedDict,
        components_carrieraccountcorreoscreaterequest.CarrierAccountCorreosCreateRequestTypedDict,
        components_carrieraccountdeutschepostcreaterequest.CarrierAccountDeutschePostCreateRequestTypedDict,
        components_carrieraccountdhlexpresscreaterequest.CarrierAccountDHLExpressCreateRequestTypedDict,
        components_carrieraccountdpddecreaterequest.CarrierAccountDpdDeCreateRequestTypedDict,
        components_carrieraccountdpdukcreaterequest.CarrierAccountDPDUKCreateRequestTypedDict,
        components_carrieraccountfedexcreaterequest.CarrierAccountFedExCreateRequestTypedDict,
        components_carrieraccounthermesukcreaterequest.CarrierAccountHermesUKCreateRequestTypedDict,
        components_carrieraccountmondialrelaycreaterequest.CarrierAccountMondialRelayCreateRequestTypedDict,
        components_carrieraccountposteitalianecreaterequest.CarrierAccountPosteItalianeCreateRequestTypedDict,
        components_carrieraccountupscreaterequest.CarrierAccountUPSCreateRequestTypedDict,
        components_carrieraccountuspscreaterequest.CarrierAccountUSPSCreateRequestTypedDict,
        components_carrieraccountsendlecreaterequest.CarrierAccountSendleCreateRequestTypedDict,
    ],
)
r"""The body of the request."""


RegisterCarrierAccountRequest = Annotated[
    Union[
        Annotated[
            components_carrieraccountcanadapostcreaterequest.CarrierAccountCanadaPostCreateRequest,
            Tag("canada_post"),
        ],
        Annotated[
            components_carrieraccountchronopostcreaterequest.CarrierAccountChronopostCreateRequest,
            Tag("chronopost"),
        ],
        Annotated[
            components_carrieraccountcolissimocreaterequest.CarrierAccountColissimoCreateRequest,
            Tag("colissimo"),
        ],
        Annotated[
            components_carrieraccountcorreoscreaterequest.CarrierAccountCorreosCreateRequest,
            Tag("correos"),
        ],
        Annotated[
            components_carrieraccountdeutschepostcreaterequest.CarrierAccountDeutschePostCreateRequest,
            Tag("deutsche_post"),
        ],
        Annotated[
            components_carrieraccountdhlexpresscreaterequest.CarrierAccountDHLExpressCreateRequest,
            Tag("dhl_express"),
        ],
        Annotated[
            components_carrieraccountdpddecreaterequest.CarrierAccountDpdDeCreateRequest,
            Tag("dpd_de"),
        ],
        Annotated[
            components_carrieraccountdpdukcreaterequest.CarrierAccountDPDUKCreateRequest,
            Tag("dpd_uk"),
        ],
        Annotated[
            components_carrieraccountfedexcreaterequest.CarrierAccountFedExCreateRequest,
            Tag("fedex"),
        ],
        Annotated[
            components_carrieraccounthermesukcreaterequest.CarrierAccountHermesUKCreateRequest,
            Tag("hermes_uk"),
        ],
        Annotated[
            components_carrieraccountmondialrelaycreaterequest.CarrierAccountMondialRelayCreateRequest,
            Tag("mondial_relay"),
        ],
        Annotated[
            components_carrieraccountposteitalianecreaterequest.CarrierAccountPosteItalianeCreateRequest,
            Tag("poste_italiane"),
        ],
        Annotated[
            components_carrieraccountupscreaterequest.CarrierAccountUPSCreateRequest,
            Tag("ups"),
        ],
        Annotated[
            components_carrieraccountuspscreaterequest.CarrierAccountUSPSCreateRequest,
            Tag("usps"),
        ],
        Annotated[
            components_carrieraccountsendlecreaterequest.CarrierAccountSendleCreateRequest,
            Tag("sendle"),
        ],
    ],
    Discriminator(lambda m: get_discriminator(m, "carrier", "carrier")),
]
r"""The body of the request."""
