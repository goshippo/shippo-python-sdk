"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .address import (
    Address,
    AddressTypedDict,
    Latitude,
    LatitudeTypedDict,
    Longitude,
    LongitudeTypedDict,
)
from .addresscompletecreaterequest import (
    AddressCompleteCreateRequest,
    AddressCompleteCreateRequestTypedDict,
)
from .addresscreaterequest import AddressCreateRequest, AddressCreateRequestTypedDict
from .addressimporter import AddressImporter, AddressImporterTypedDict
from .addresspaginatedlist import AddressPaginatedList, AddressPaginatedListTypedDict
from .addressvalidationresults import (
    AddressValidationResults,
    AddressValidationResultsTypedDict,
)
from .addressvalidationresultsmessage import (
    AddressValidationResultsMessage,
    AddressValidationResultsMessageTypedDict,
)
from .addressvalidationresultsmessagecodeenum import (
    AddressValidationResultsMessageCodeEnum,
)
from .addressvalidationresultsmessagesourceenum import (
    AddressValidationResultsMessageSourceEnum,
)
from .alcohol import Alcohol, AlcoholTypedDict, RecipientType
from .batch import (
    Batch,
    BatchStatus,
    BatchTypedDict,
    ObjectResults,
    ObjectResultsTypedDict,
)
from .batchcreaterequest import BatchCreateRequest, BatchCreateRequestTypedDict
from .batchshipment import BatchShipment, BatchShipmentStatus, BatchShipmentTypedDict
from .batchshipmentcreaterequest import (
    BatchShipmentCreateRequest,
    BatchShipmentCreateRequestTypedDict,
)
from .batchshipmentpaginatedlist import (
    BatchShipmentPaginatedList,
    BatchShipmentPaginatedListTypedDict,
)
from .billing import Billing, BillingType, BillingTypedDict
from .carrieraccount import (
    CarrierAccount,
    CarrierAccountParameters,
    CarrierAccountParametersTypedDict,
    CarrierAccountTypedDict,
)
from .carrieraccountbase import (
    CarrierAccountBase,
    CarrierAccountBaseParameters,
    CarrierAccountBaseParametersTypedDict,
    CarrierAccountBaseTypedDict,
)
from .carrieraccountcanadapostcreateparameters import (
    CarrierAccountCanadaPostCreateParameters,
    CarrierAccountCanadaPostCreateParametersTypedDict,
)
from .carrieraccountcanadapostcreaterequest import (
    CarrierAccountCanadaPostCreateRequest,
    CarrierAccountCanadaPostCreateRequestTypedDict,
)
from .carrieraccountchronopostcreaterequest import (
    CarrierAccountChronopostCreateRequest,
    CarrierAccountChronopostCreateRequestParameters,
    CarrierAccountChronopostCreateRequestParametersTypedDict,
    CarrierAccountChronopostCreateRequestTypedDict,
)
from .carrieraccountcolissimocreaterequest import (
    CarrierAccountColissimoCreateRequest,
    CarrierAccountColissimoCreateRequestParameters,
    CarrierAccountColissimoCreateRequestParametersTypedDict,
    CarrierAccountColissimoCreateRequestTypedDict,
)
from .carrieraccountcorreoscreaterequest import (
    CarrierAccountCorreosCreateRequest,
    CarrierAccountCorreosCreateRequestParameters,
    CarrierAccountCorreosCreateRequestParametersTypedDict,
    CarrierAccountCorreosCreateRequestTypedDict,
)
from .carrieraccountdeutschepostcreaterequest import (
    CarrierAccountDeutschePostCreateRequest,
    CarrierAccountDeutschePostCreateRequestParameters,
    CarrierAccountDeutschePostCreateRequestParametersTypedDict,
    CarrierAccountDeutschePostCreateRequestTypedDict,
)
from .carrieraccountdhlexpresscreaterequest import (
    CarrierAccountDHLExpressCreateRequest,
    CarrierAccountDHLExpressCreateRequestTypedDict,
)
from .carrieraccountdhlexpresscreaterequestparameters import (
    CarrierAccountDHLExpressCreateRequestParameters,
    CarrierAccountDHLExpressCreateRequestParametersTypedDict,
)
from .carrieraccountdpddecreaterequest import (
    CarrierAccountDpdDeCreateRequest,
    CarrierAccountDpdDeCreateRequestParameters,
    CarrierAccountDpdDeCreateRequestParametersTypedDict,
    CarrierAccountDpdDeCreateRequestTypedDict,
)
from .carrieraccountdpdukcreaterequest import (
    CarrierAccountDPDUKCreateRequest,
    CarrierAccountDPDUKCreateRequestParameters,
    CarrierAccountDPDUKCreateRequestParametersTypedDict,
    CarrierAccountDPDUKCreateRequestTypedDict,
)
from .carrieraccountfedexcreaterequest import (
    CarrierAccountFedExCreateRequest,
    CarrierAccountFedExCreateRequestParameters,
    CarrierAccountFedExCreateRequestParametersTypedDict,
    CarrierAccountFedExCreateRequestTypedDict,
)
from .carrieraccounthermesukcreaterequest import (
    CarrierAccountHermesUKCreateRequest,
    CarrierAccountHermesUKCreateRequestParameters,
    CarrierAccountHermesUKCreateRequestParametersTypedDict,
    CarrierAccountHermesUKCreateRequestTypedDict,
)
from .carrieraccountmondialrelaycreaterequest import (
    CarrierAccountMondialRelayCreateRequest,
    CarrierAccountMondialRelayCreateRequestParameters,
    CarrierAccountMondialRelayCreateRequestParametersTypedDict,
    CarrierAccountMondialRelayCreateRequestTypedDict,
)
from .carrieraccountpaginatedlist import (
    CarrierAccountPaginatedList,
    CarrierAccountPaginatedListTypedDict,
)
from .carrieraccountposteitalianecreaterequest import (
    CarrierAccountPosteItalianeCreateRequest,
    CarrierAccountPosteItalianeCreateRequestParameters,
    CarrierAccountPosteItalianeCreateRequestParametersTypedDict,
    CarrierAccountPosteItalianeCreateRequestTypedDict,
)
from .carrieraccountregistrationstatus import (
    CarrierAccountRegistrationStatus,
    CarrierAccountRegistrationStatusTypedDict,
)
from .carrieraccountsendlecreaterequest import (
    CarrierAccountSendleCreateRequest,
    CarrierAccountSendleCreateRequestParameters,
    CarrierAccountSendleCreateRequestParametersTypedDict,
    CarrierAccountSendleCreateRequestTypedDict,
)
from .carrieraccountservicelevel import (
    CarrierAccountServiceLevel,
    CarrierAccountServiceLevelTypedDict,
)
from .carrieraccountupscreaterequest import (
    CarrierAccountUPSCreateRequest,
    CarrierAccountUPSCreateRequestTypedDict,
)
from .carrieraccountupscreaterequestparameters import (
    CarrierAccountUPSCreateRequestParameters,
    CarrierAccountUPSCreateRequestParametersTypedDict,
)
from .carrieraccountuspscreaterequest import (
    CarrierAccountUSPSCreateRequest,
    CarrierAccountUSPSCreateRequestParameters,
    CarrierAccountUSPSCreateRequestParametersTypedDict,
    CarrierAccountUSPSCreateRequestTypedDict,
)
from .carrieraccountwithextrainfo import (
    Authentication,
    AuthenticationTypedDict,
    CarrierAccountWithExtraInfo,
    CarrierAccountWithExtraInfoParameters,
    CarrierAccountWithExtraInfoParametersTypedDict,
    CarrierAccountWithExtraInfoStatus,
    CarrierAccountWithExtraInfoType,
    CarrierAccountWithExtraInfoTypedDict,
    ObjectInfo,
    ObjectInfoTypedDict,
)
from .carrierparceltemplate import CarrierParcelTemplate, CarrierParcelTemplateTypedDict
from .carrierparceltemplatelist import (
    CarrierParcelTemplateList,
    CarrierParcelTemplateListTypedDict,
)
from .carriersenum import CarriersEnum
from .cod import Cod, CodTypedDict, PaymentMethod
from .connectexistingownaccountrequest import (
    ConnectExistingOwnAccountRequest,
    ConnectExistingOwnAccountRequestParameters,
    ConnectExistingOwnAccountRequestParametersTypedDict,
    ConnectExistingOwnAccountRequestTypedDict,
)
from .corerate import CoreRate, CoreRateTypedDict
from .customerreference import CustomerReference, CustomerReferenceTypedDict
from .customsdeclaration import (
    CustomsDeclaration,
    CustomsDeclarationAddress,
    CustomsDeclarationAddressTypedDict,
    CustomsDeclarationDutiesPayor,
    CustomsDeclarationDutiesPayorTypedDict,
    CustomsDeclarationType,
    CustomsDeclarationTypedDict,
)
from .customsdeclarationb13afilingoptionenum import (
    CustomsDeclarationB13AFilingOptionEnum,
)
from .customsdeclarationcontentstypeenum import CustomsDeclarationContentsTypeEnum
from .customsdeclarationcreaterequest import (
    CustomsDeclarationCreateRequest,
    CustomsDeclarationCreateRequestAddress,
    CustomsDeclarationCreateRequestAddressTypedDict,
    CustomsDeclarationCreateRequestDutiesPayor,
    CustomsDeclarationCreateRequestDutiesPayorTypedDict,
    CustomsDeclarationCreateRequestType,
    CustomsDeclarationCreateRequestTypedDict,
)
from .customsdeclarationeelpfcenum import CustomsDeclarationEelPfcEnum
from .customsdeclarationincotermenum import CustomsDeclarationIncotermEnum
from .customsdeclarationnondeliveryoptionenum import (
    CustomsDeclarationNonDeliveryOptionEnum,
)
from .customsdeclarationpaginatedlist import (
    CustomsDeclarationPaginatedList,
    CustomsDeclarationPaginatedListTypedDict,
)
from .customsexporteridentification import (
    CustomsExporterIdentification,
    CustomsExporterIdentificationTypedDict,
)
from .customsinvoicedcharges import (
    CustomsInvoicedCharges,
    CustomsInvoicedChargesTypedDict,
)
from .customsitem import CustomsItem, CustomsItemTypedDict
from .customsitemcreaterequest import (
    CustomsItemCreateRequest,
    CustomsItemCreateRequestTypedDict,
)
from .customsitempaginatedlist import (
    CustomsItemPaginatedList,
    CustomsItemPaginatedListTypedDict,
)
from .customstaxidentification import (
    CustomsTaxIdentification,
    CustomsTaxIdentificationType,
    CustomsTaxIdentificationTypedDict,
)
from .dangerousgoodsbiologicalmaterial import (
    DangerousGoodsBiologicalMaterial,
    DangerousGoodsBiologicalMaterialTypedDict,
)
from .dangerousgoodslithiumbatteries import (
    DangerousGoodsLithiumBatteries,
    DangerousGoodsLithiumBatteriesTypedDict,
)
from .dangerousgoodsobject import DangerousGoodsObject, DangerousGoodsObjectTypedDict
from .defaultparceltemplate import DefaultParcelTemplate, DefaultParcelTemplateTypedDict
from .defaultparceltemplateupdaterequest import (
    DefaultParcelTemplateUpdateRequest,
    DefaultParcelTemplateUpdateRequestTypedDict,
)
from .departmentnumber import DepartmentNumber, DepartmentNumberTypedDict
from .distanceunitenum import DistanceUnitEnum
from .dryice import DryIce, DryIceTypedDict
from .fedexconnectexistingownaccountparameters import (
    FedExConnectExistingOwnAccountParameters,
    FedExConnectExistingOwnAccountParametersTypedDict,
)
from .instanttransactioncreaterequest import (
    InstantTransactionCreateRequest,
    InstantTransactionCreateRequestTypedDict,
    LabelFileType,
)
from .insurance import Insurance, InsuranceProvider, InsuranceTypedDict
from .invoicenumber import InvoiceNumber, InvoiceNumberTypedDict
from .labelfiletypeenum import LabelFileTypeEnum
from .lineitem import LineItem, LineItemTypedDict
from .lineitembase import LineItemBase, LineItemBaseTypedDict
from .liverate import LiveRate, LiveRateTypedDict
from .liveratecreaterequest import (
    LiveRateCreateRequest,
    LiveRateCreateRequestAddressFrom,
    LiveRateCreateRequestAddressFromTypedDict,
    LiveRateCreateRequestAddressTo,
    LiveRateCreateRequestAddressToTypedDict,
    LiveRateCreateRequestParcel,
    LiveRateCreateRequestParcelTypedDict,
    LiveRateCreateRequestTypedDict,
)
from .liveratepaginatedlist import LiveRatePaginatedList, LiveRatePaginatedListTypedDict
from .location import BuildingLocationType, BuildingType, Location, LocationTypedDict
from .manifest import Manifest, ManifestStatus, ManifestTypedDict
from .manifestcreaterequest import (
    ManifestCreateRequest,
    ManifestCreateRequestAddressFrom,
    ManifestCreateRequestAddressFromTypedDict,
    ManifestCreateRequestTypedDict,
)
from .manifestpaginatedlist import ManifestPaginatedList, ManifestPaginatedListTypedDict
from .objectstateenum import ObjectStateEnum
from .order import Order, OrderTransaction, OrderTransactionTypedDict, OrderTypedDict
from .ordercreaterequest import OrderCreateRequest, OrderCreateRequestTypedDict
from .orderpaginatedlist import OrderPaginatedList, OrderPaginatedListTypedDict
from .ordershopappenum import OrderShopAppEnum
from .orderstatusenum import OrderStatusEnum
from .parcel import ObjectState, Parcel, ParcelTypedDict
from .parcelcreatefromtemplaterequest import (
    ParcelCreateFromTemplateRequest,
    ParcelCreateFromTemplateRequestTypedDict,
)
from .parcelcreaterequest import ParcelCreateRequest, ParcelCreateRequestTypedDict
from .parcelextra import ParcelExtra, ParcelExtraTypedDict
from .parcelinsurance import (
    ParcelInsurance,
    ParcelInsuranceProvider,
    ParcelInsuranceTypedDict,
)
from .parcelpaginatedlist import ParcelPaginatedList, ParcelPaginatedListTypedDict
from .parceltemplatearamexaustraliaenum import ParcelTemplateAramexAustraliaEnum
from .parceltemplatedhlecommerceenum import ParcelTemplateDHLeCommerceEnum
from .parceltemplatedpdukenum import ParcelTemplateDPDUKEnum
from .parceltemplateenumset import ParcelTemplateEnumSet, ParcelTemplateEnumSetTypedDict
from .parceltemplatefedexenum import ParcelTemplateFedExEnum
from .parceltemplateupsenum import ParcelTemplateUPSEnum
from .parceltemplateuspsenum import ParcelTemplateUSPSEnum
from .pickup import Pickup, PickupStatus, PickupTypedDict
from .pickupbase import PickupBase, PickupBaseTypedDict
from .ponumber import PoNumber, PoNumberTypedDict
from .rate import Attribute, Rate, RateTypedDict
from .ratepaginatedlist import RatePaginatedList, RatePaginatedListTypedDict
from .refund import Refund, RefundStatus, RefundTypedDict
from .refundpaginatedlist import RefundPaginatedList, RefundPaginatedListTypedDict
from .refundrequestbody import RefundRequestBody, RefundRequestBodyTypedDict
from .responsemessage import ResponseMessage, ResponseMessageTypedDict
from .rmanumber import RmaNumber, RmaNumberTypedDict
from .security import Security, SecurityTypedDict
from .servicegroup import ServiceGroup, ServiceGroupTypedDict
from .servicegroupaccountandservicelevel import (
    ServiceGroupAccountAndServiceLevel,
    ServiceGroupAccountAndServiceLevelTypedDict,
)
from .servicegroupcreaterequest import (
    ServiceGroupCreateRequest,
    ServiceGroupCreateRequestTypedDict,
)
from .servicegrouptypeenum import ServiceGroupTypeEnum
from .servicegroupupdaterequest import (
    ServiceGroupUpdateRequest,
    ServiceGroupUpdateRequestTypedDict,
)
from .servicelevel import ServiceLevel, ServiceLevelTypedDict
from .servicelevelairterraenum import ServiceLevelAirterraEnum
from .servicelevelapcpostalenum import ServiceLevelAPCPostalEnum
from .servicelevelapgenum import ServiceLevelAPGEnum
from .servicelevelaramexaustraliaenum import ServiceLevelAramexAustraliaEnum
from .servicelevelasendiaenum import ServiceLevelAsendiaEnum
from .servicelevelaustraliapostenum import ServiceLevelAustraliaPostEnum
from .servicelevelbettertrucksenum import ServiceLevelBetterTrucksEnum
from .servicelevelcanadapostenum import ServiceLevelCanadaPostEnum
from .servicelevelcdlenum import ServiceLevelCDLEnum
from .servicelevelchronopostenum import ServiceLevelChronopostEnum
from .servicelevelcolissimoenum import ServiceLevelColissimoEnum
from .servicelevelcorreosespanaenum import ServiceLevelCorreosEspanaEnum
from .serviceleveldeutschepostenum import ServiceLevelDeutschePostEnum
from .serviceleveldhlecommerceenum import ServiceLevelDHLeCommerceEnum
from .serviceleveldhlexpressenum import ServiceLevelDHLExpressEnum
from .serviceleveldhlgermanyenum import ServiceLevelDHLGermanyEnum
from .serviceleveldpddeenum import ServiceLevelDPDDEEnum
from .serviceleveldpdukenum import ServiceLevelDPDUKEnum
from .servicelevelenumset import ServiceLevelEnumSet, ServiceLevelEnumSetTypedDict
from .servicelevelepostglobalenum import ServiceLevelePostGlobalEnum
from .servicelevelevriukenum import ServiceLevelEvriUKEnum
from .servicelevelfedexenum import ServiceLevelFedExEnum
from .servicelevelglobegisticsenum import ServiceLevelGlobegisticsEnum
from .servicelevelglsusenum import ServiceLevelGLSUSEnum
from .serviceleveljitsuenum import ServiceLevelJitsuEnum
from .servicelevellasershipenum import ServiceLevelLasershipEnum
from .servicelevellsoenum import ServiceLevelLSOEnum
from .servicelevelmondialrelayenum import ServiceLevelMondialRelayEnum
from .servicelevelontracenum import ServiceLevelOnTracEnum
from .servicelevelparcelforceenum import ServiceLevelParcelforceEnum
from .servicelevelpostitalianeenum import ServiceLevelPostItalianeEnum
from .servicelevelpurolatorenum import ServiceLevelPurolatorEnum
from .servicelevelroyalmailenum import ServiceLevelRoyalMailEnum
from .servicelevelsendleenum import ServiceLevelSendleEnum
from .servicelevelswyftenum import ServiceLevelSwyftEnum
from .serviceleveludsenum import ServiceLevelUDSEnum
from .servicelevelupsenum import ServiceLevelUPSEnum
from .serviceleveluspsenum import ServiceLevelUSPSEnum
from .servicelevelvehoenum import ServiceLevelVehoEnum
from .servicelevelwithparent import (
    ServiceLevelWithParent,
    ServiceLevelWithParentTypedDict,
)
from .shipment import Shipment, ShipmentStatus, ShipmentTypedDict
from .shipmentcreaterequest import (
    AddressReturn,
    AddressReturnTypedDict,
    CustomsDeclarationUnion,
    CustomsDeclarationUnionTypedDict,
    ShipmentCreateRequest,
    ShipmentCreateRequestAddressFrom,
    ShipmentCreateRequestAddressFromTypedDict,
    ShipmentCreateRequestAddressTo,
    ShipmentCreateRequestAddressToTypedDict,
    ShipmentCreateRequestParcel,
    ShipmentCreateRequestParcelTypedDict,
    ShipmentCreateRequestTypedDict,
)
from .shipmentextra import (
    AncillaryEndorsement,
    DangerousGoodsCode,
    PreferredDeliveryTimeframe,
    ReturnServiceType,
    ReturnServiceTypeTypedDict,
    ShipmentExtra,
    ShipmentExtraTypedDict,
    SignatureConfirmation,
)
from .shipmentextralasershipattributesenum import ShipmentExtraLasershipAttributesEnum
from .shipmentextrareturnservicetypelasershipenum import (
    ShipmentExtraReturnServiceTypeLasershipEnum,
)
from .shipmentextrareturnservicetypeupsenum import ShipmentExtraReturnServiceTypeUPSEnum
from .shipmentpaginatedlist import ShipmentPaginatedList, ShipmentPaginatedListTypedDict
from .shippoaccount import ShippoAccount, ShippoAccountTypedDict
from .shippoaccountpaginatedlist import (
    ShippoAccountPaginatedList,
    ShippoAccountPaginatedListTypedDict,
)
from .shippoaccountupdaterequest import (
    ShippoAccountUpdateRequest,
    ShippoAccountUpdateRequestTypedDict,
)
from .track import Track, TrackTypedDict
from .trackingstatus import TrackingStatus, TrackingStatusTypedDict
from .trackingstatusenum import TrackingStatusEnum
from .trackingstatuslocationbase import (
    TrackingStatusLocationBase,
    TrackingStatusLocationBaseTypedDict,
)
from .trackingstatussubstatus import (
    TrackingStatusSubstatus,
    TrackingStatusSubstatusTypedDict,
)
from .tracksrequest import TracksRequest, TracksRequestTypedDict
from .transaction import (
    CreatedBy,
    CreatedByTypedDict,
    RateUnion,
    RateUnionTypedDict,
    Transaction,
    TransactionTypedDict,
)
from .transactioncreaterequest import (
    TransactionCreateRequest,
    TransactionCreateRequestTypedDict,
)
from .transactionpaginatedlist import (
    TransactionPaginatedList,
    TransactionPaginatedListTypedDict,
)
from .transactionstatusenum import TransactionStatusEnum
from .upsconnectexistingownaccountparameters import (
    UPSConnectExistingOwnAccountParameters,
    UPSConnectExistingOwnAccountParametersTypedDict,
)
from .upsreferencefields import UPSReferenceFields, UPSReferenceFieldsTypedDict
from .userparceltemplate import UserParcelTemplate, UserParcelTemplateTypedDict
from .userparceltemplatecreaterequest import (
    UserParcelTemplateCreateRequest,
    UserParcelTemplateCreateRequestTypedDict,
)
from .userparceltemplatelist import (
    UserParcelTemplateList,
    UserParcelTemplateListTypedDict,
)
from .userparceltemplateupdaterequest import (
    UserParcelTemplateUpdateRequest,
    UserParcelTemplateUpdateRequestTypedDict,
)
from .userparceltemplatewithcarriertemplatecreaterequest import (
    UserParcelTemplateWithCarrierTemplateCreateRequest,
    UserParcelTemplateWithCarrierTemplateCreateRequestTypedDict,
)
from .userparceltemplatewithoutcarriertemplatecreaterequest import (
    UserParcelTemplateWithoutCarrierTemplateCreateRequest,
    UserParcelTemplateWithoutCarrierTemplateCreateRequestTypedDict,
)
from .webhook import Webhook, WebhookTypedDict
from .webhookeventtypeenum import WebhookEventTypeEnum
from .webhookpaginatedlist import WebhookPaginatedList, WebhookPaginatedListTypedDict
from .webhookpayload import WebhookPayload, WebhookPayloadTypedDict
from .webhookpayloadbatch import WebhookPayloadBatch, WebhookPayloadBatchTypedDict
from .webhookpayloadtrack import WebhookPayloadTrack, WebhookPayloadTrackTypedDict
from .webhookpayloadtransaction import (
    WebhookPayloadTransaction,
    WebhookPayloadTransactionTypedDict,
)
from .webhookupdaterequest import WebhookUpdateRequest, WebhookUpdateRequestTypedDict
from .weightunitenum import WeightUnitEnum


__all__ = [
    "Address",
    "AddressCompleteCreateRequest",
    "AddressCompleteCreateRequestTypedDict",
    "AddressCreateRequest",
    "AddressCreateRequestTypedDict",
    "AddressImporter",
    "AddressImporterTypedDict",
    "AddressPaginatedList",
    "AddressPaginatedListTypedDict",
    "AddressReturn",
    "AddressReturnTypedDict",
    "AddressTypedDict",
    "AddressValidationResults",
    "AddressValidationResultsMessage",
    "AddressValidationResultsMessageCodeEnum",
    "AddressValidationResultsMessageSourceEnum",
    "AddressValidationResultsMessageTypedDict",
    "AddressValidationResultsTypedDict",
    "Alcohol",
    "AlcoholTypedDict",
    "AncillaryEndorsement",
    "Attribute",
    "Authentication",
    "AuthenticationTypedDict",
    "Batch",
    "BatchCreateRequest",
    "BatchCreateRequestTypedDict",
    "BatchShipment",
    "BatchShipmentCreateRequest",
    "BatchShipmentCreateRequestTypedDict",
    "BatchShipmentPaginatedList",
    "BatchShipmentPaginatedListTypedDict",
    "BatchShipmentStatus",
    "BatchShipmentTypedDict",
    "BatchStatus",
    "BatchTypedDict",
    "Billing",
    "BillingType",
    "BillingTypedDict",
    "BuildingLocationType",
    "BuildingType",
    "CarrierAccount",
    "CarrierAccountBase",
    "CarrierAccountBaseParameters",
    "CarrierAccountBaseParametersTypedDict",
    "CarrierAccountBaseTypedDict",
    "CarrierAccountCanadaPostCreateParameters",
    "CarrierAccountCanadaPostCreateParametersTypedDict",
    "CarrierAccountCanadaPostCreateRequest",
    "CarrierAccountCanadaPostCreateRequestTypedDict",
    "CarrierAccountChronopostCreateRequest",
    "CarrierAccountChronopostCreateRequestParameters",
    "CarrierAccountChronopostCreateRequestParametersTypedDict",
    "CarrierAccountChronopostCreateRequestTypedDict",
    "CarrierAccountColissimoCreateRequest",
    "CarrierAccountColissimoCreateRequestParameters",
    "CarrierAccountColissimoCreateRequestParametersTypedDict",
    "CarrierAccountColissimoCreateRequestTypedDict",
    "CarrierAccountCorreosCreateRequest",
    "CarrierAccountCorreosCreateRequestParameters",
    "CarrierAccountCorreosCreateRequestParametersTypedDict",
    "CarrierAccountCorreosCreateRequestTypedDict",
    "CarrierAccountDHLExpressCreateRequest",
    "CarrierAccountDHLExpressCreateRequestParameters",
    "CarrierAccountDHLExpressCreateRequestParametersTypedDict",
    "CarrierAccountDHLExpressCreateRequestTypedDict",
    "CarrierAccountDPDUKCreateRequest",
    "CarrierAccountDPDUKCreateRequestParameters",
    "CarrierAccountDPDUKCreateRequestParametersTypedDict",
    "CarrierAccountDPDUKCreateRequestTypedDict",
    "CarrierAccountDeutschePostCreateRequest",
    "CarrierAccountDeutschePostCreateRequestParameters",
    "CarrierAccountDeutschePostCreateRequestParametersTypedDict",
    "CarrierAccountDeutschePostCreateRequestTypedDict",
    "CarrierAccountDpdDeCreateRequest",
    "CarrierAccountDpdDeCreateRequestParameters",
    "CarrierAccountDpdDeCreateRequestParametersTypedDict",
    "CarrierAccountDpdDeCreateRequestTypedDict",
    "CarrierAccountFedExCreateRequest",
    "CarrierAccountFedExCreateRequestParameters",
    "CarrierAccountFedExCreateRequestParametersTypedDict",
    "CarrierAccountFedExCreateRequestTypedDict",
    "CarrierAccountHermesUKCreateRequest",
    "CarrierAccountHermesUKCreateRequestParameters",
    "CarrierAccountHermesUKCreateRequestParametersTypedDict",
    "CarrierAccountHermesUKCreateRequestTypedDict",
    "CarrierAccountMondialRelayCreateRequest",
    "CarrierAccountMondialRelayCreateRequestParameters",
    "CarrierAccountMondialRelayCreateRequestParametersTypedDict",
    "CarrierAccountMondialRelayCreateRequestTypedDict",
    "CarrierAccountPaginatedList",
    "CarrierAccountPaginatedListTypedDict",
    "CarrierAccountParameters",
    "CarrierAccountParametersTypedDict",
    "CarrierAccountPosteItalianeCreateRequest",
    "CarrierAccountPosteItalianeCreateRequestParameters",
    "CarrierAccountPosteItalianeCreateRequestParametersTypedDict",
    "CarrierAccountPosteItalianeCreateRequestTypedDict",
    "CarrierAccountRegistrationStatus",
    "CarrierAccountRegistrationStatusTypedDict",
    "CarrierAccountSendleCreateRequest",
    "CarrierAccountSendleCreateRequestParameters",
    "CarrierAccountSendleCreateRequestParametersTypedDict",
    "CarrierAccountSendleCreateRequestTypedDict",
    "CarrierAccountServiceLevel",
    "CarrierAccountServiceLevelTypedDict",
    "CarrierAccountTypedDict",
    "CarrierAccountUPSCreateRequest",
    "CarrierAccountUPSCreateRequestParameters",
    "CarrierAccountUPSCreateRequestParametersTypedDict",
    "CarrierAccountUPSCreateRequestTypedDict",
    "CarrierAccountUSPSCreateRequest",
    "CarrierAccountUSPSCreateRequestParameters",
    "CarrierAccountUSPSCreateRequestParametersTypedDict",
    "CarrierAccountUSPSCreateRequestTypedDict",
    "CarrierAccountWithExtraInfo",
    "CarrierAccountWithExtraInfoParameters",
    "CarrierAccountWithExtraInfoParametersTypedDict",
    "CarrierAccountWithExtraInfoStatus",
    "CarrierAccountWithExtraInfoType",
    "CarrierAccountWithExtraInfoTypedDict",
    "CarrierParcelTemplate",
    "CarrierParcelTemplateList",
    "CarrierParcelTemplateListTypedDict",
    "CarrierParcelTemplateTypedDict",
    "CarriersEnum",
    "Cod",
    "CodTypedDict",
    "ConnectExistingOwnAccountRequest",
    "ConnectExistingOwnAccountRequestParameters",
    "ConnectExistingOwnAccountRequestParametersTypedDict",
    "ConnectExistingOwnAccountRequestTypedDict",
    "CoreRate",
    "CoreRateTypedDict",
    "CreatedBy",
    "CreatedByTypedDict",
    "CustomerReference",
    "CustomerReferenceTypedDict",
    "CustomsDeclaration",
    "CustomsDeclarationAddress",
    "CustomsDeclarationAddressTypedDict",
    "CustomsDeclarationB13AFilingOptionEnum",
    "CustomsDeclarationContentsTypeEnum",
    "CustomsDeclarationCreateRequest",
    "CustomsDeclarationCreateRequestAddress",
    "CustomsDeclarationCreateRequestAddressTypedDict",
    "CustomsDeclarationCreateRequestDutiesPayor",
    "CustomsDeclarationCreateRequestDutiesPayorTypedDict",
    "CustomsDeclarationCreateRequestType",
    "CustomsDeclarationCreateRequestTypedDict",
    "CustomsDeclarationDutiesPayor",
    "CustomsDeclarationDutiesPayorTypedDict",
    "CustomsDeclarationEelPfcEnum",
    "CustomsDeclarationIncotermEnum",
    "CustomsDeclarationNonDeliveryOptionEnum",
    "CustomsDeclarationPaginatedList",
    "CustomsDeclarationPaginatedListTypedDict",
    "CustomsDeclarationType",
    "CustomsDeclarationTypedDict",
    "CustomsDeclarationUnion",
    "CustomsDeclarationUnionTypedDict",
    "CustomsExporterIdentification",
    "CustomsExporterIdentificationTypedDict",
    "CustomsInvoicedCharges",
    "CustomsInvoicedChargesTypedDict",
    "CustomsItem",
    "CustomsItemCreateRequest",
    "CustomsItemCreateRequestTypedDict",
    "CustomsItemPaginatedList",
    "CustomsItemPaginatedListTypedDict",
    "CustomsItemTypedDict",
    "CustomsTaxIdentification",
    "CustomsTaxIdentificationType",
    "CustomsTaxIdentificationTypedDict",
    "DangerousGoodsBiologicalMaterial",
    "DangerousGoodsBiologicalMaterialTypedDict",
    "DangerousGoodsCode",
    "DangerousGoodsLithiumBatteries",
    "DangerousGoodsLithiumBatteriesTypedDict",
    "DangerousGoodsObject",
    "DangerousGoodsObjectTypedDict",
    "DefaultParcelTemplate",
    "DefaultParcelTemplateTypedDict",
    "DefaultParcelTemplateUpdateRequest",
    "DefaultParcelTemplateUpdateRequestTypedDict",
    "DepartmentNumber",
    "DepartmentNumberTypedDict",
    "DistanceUnitEnum",
    "DryIce",
    "DryIceTypedDict",
    "FedExConnectExistingOwnAccountParameters",
    "FedExConnectExistingOwnAccountParametersTypedDict",
    "InstantTransactionCreateRequest",
    "InstantTransactionCreateRequestTypedDict",
    "Insurance",
    "InsuranceProvider",
    "InsuranceTypedDict",
    "InvoiceNumber",
    "InvoiceNumberTypedDict",
    "LabelFileType",
    "LabelFileTypeEnum",
    "Latitude",
    "LatitudeTypedDict",
    "LineItem",
    "LineItemBase",
    "LineItemBaseTypedDict",
    "LineItemTypedDict",
    "LiveRate",
    "LiveRateCreateRequest",
    "LiveRateCreateRequestAddressFrom",
    "LiveRateCreateRequestAddressFromTypedDict",
    "LiveRateCreateRequestAddressTo",
    "LiveRateCreateRequestAddressToTypedDict",
    "LiveRateCreateRequestParcel",
    "LiveRateCreateRequestParcelTypedDict",
    "LiveRateCreateRequestTypedDict",
    "LiveRatePaginatedList",
    "LiveRatePaginatedListTypedDict",
    "LiveRateTypedDict",
    "Location",
    "LocationTypedDict",
    "Longitude",
    "LongitudeTypedDict",
    "Manifest",
    "ManifestCreateRequest",
    "ManifestCreateRequestAddressFrom",
    "ManifestCreateRequestAddressFromTypedDict",
    "ManifestCreateRequestTypedDict",
    "ManifestPaginatedList",
    "ManifestPaginatedListTypedDict",
    "ManifestStatus",
    "ManifestTypedDict",
    "ObjectInfo",
    "ObjectInfoTypedDict",
    "ObjectResults",
    "ObjectResultsTypedDict",
    "ObjectState",
    "ObjectStateEnum",
    "Order",
    "OrderCreateRequest",
    "OrderCreateRequestTypedDict",
    "OrderPaginatedList",
    "OrderPaginatedListTypedDict",
    "OrderShopAppEnum",
    "OrderStatusEnum",
    "OrderTransaction",
    "OrderTransactionTypedDict",
    "OrderTypedDict",
    "Parcel",
    "ParcelCreateFromTemplateRequest",
    "ParcelCreateFromTemplateRequestTypedDict",
    "ParcelCreateRequest",
    "ParcelCreateRequestTypedDict",
    "ParcelExtra",
    "ParcelExtraTypedDict",
    "ParcelInsurance",
    "ParcelInsuranceProvider",
    "ParcelInsuranceTypedDict",
    "ParcelPaginatedList",
    "ParcelPaginatedListTypedDict",
    "ParcelTemplateAramexAustraliaEnum",
    "ParcelTemplateDHLeCommerceEnum",
    "ParcelTemplateDPDUKEnum",
    "ParcelTemplateEnumSet",
    "ParcelTemplateEnumSetTypedDict",
    "ParcelTemplateFedExEnum",
    "ParcelTemplateUPSEnum",
    "ParcelTemplateUSPSEnum",
    "ParcelTypedDict",
    "PaymentMethod",
    "Pickup",
    "PickupBase",
    "PickupBaseTypedDict",
    "PickupStatus",
    "PickupTypedDict",
    "PoNumber",
    "PoNumberTypedDict",
    "PreferredDeliveryTimeframe",
    "Rate",
    "RatePaginatedList",
    "RatePaginatedListTypedDict",
    "RateTypedDict",
    "RateUnion",
    "RateUnionTypedDict",
    "RecipientType",
    "Refund",
    "RefundPaginatedList",
    "RefundPaginatedListTypedDict",
    "RefundRequestBody",
    "RefundRequestBodyTypedDict",
    "RefundStatus",
    "RefundTypedDict",
    "ResponseMessage",
    "ResponseMessageTypedDict",
    "ReturnServiceType",
    "ReturnServiceTypeTypedDict",
    "RmaNumber",
    "RmaNumberTypedDict",
    "Security",
    "SecurityTypedDict",
    "ServiceGroup",
    "ServiceGroupAccountAndServiceLevel",
    "ServiceGroupAccountAndServiceLevelTypedDict",
    "ServiceGroupCreateRequest",
    "ServiceGroupCreateRequestTypedDict",
    "ServiceGroupTypeEnum",
    "ServiceGroupTypedDict",
    "ServiceGroupUpdateRequest",
    "ServiceGroupUpdateRequestTypedDict",
    "ServiceLevel",
    "ServiceLevelAPCPostalEnum",
    "ServiceLevelAPGEnum",
    "ServiceLevelAirterraEnum",
    "ServiceLevelAramexAustraliaEnum",
    "ServiceLevelAsendiaEnum",
    "ServiceLevelAustraliaPostEnum",
    "ServiceLevelBetterTrucksEnum",
    "ServiceLevelCDLEnum",
    "ServiceLevelCanadaPostEnum",
    "ServiceLevelChronopostEnum",
    "ServiceLevelColissimoEnum",
    "ServiceLevelCorreosEspanaEnum",
    "ServiceLevelDHLExpressEnum",
    "ServiceLevelDHLGermanyEnum",
    "ServiceLevelDHLeCommerceEnum",
    "ServiceLevelDPDDEEnum",
    "ServiceLevelDPDUKEnum",
    "ServiceLevelDeutschePostEnum",
    "ServiceLevelEnumSet",
    "ServiceLevelEnumSetTypedDict",
    "ServiceLevelEvriUKEnum",
    "ServiceLevelFedExEnum",
    "ServiceLevelGLSUSEnum",
    "ServiceLevelGlobegisticsEnum",
    "ServiceLevelJitsuEnum",
    "ServiceLevelLSOEnum",
    "ServiceLevelLasershipEnum",
    "ServiceLevelMondialRelayEnum",
    "ServiceLevelOnTracEnum",
    "ServiceLevelParcelforceEnum",
    "ServiceLevelPostItalianeEnum",
    "ServiceLevelPurolatorEnum",
    "ServiceLevelRoyalMailEnum",
    "ServiceLevelSendleEnum",
    "ServiceLevelSwyftEnum",
    "ServiceLevelTypedDict",
    "ServiceLevelUDSEnum",
    "ServiceLevelUPSEnum",
    "ServiceLevelUSPSEnum",
    "ServiceLevelVehoEnum",
    "ServiceLevelWithParent",
    "ServiceLevelWithParentTypedDict",
    "ServiceLevelePostGlobalEnum",
    "Shipment",
    "ShipmentCreateRequest",
    "ShipmentCreateRequestAddressFrom",
    "ShipmentCreateRequestAddressFromTypedDict",
    "ShipmentCreateRequestAddressTo",
    "ShipmentCreateRequestAddressToTypedDict",
    "ShipmentCreateRequestParcel",
    "ShipmentCreateRequestParcelTypedDict",
    "ShipmentCreateRequestTypedDict",
    "ShipmentExtra",
    "ShipmentExtraLasershipAttributesEnum",
    "ShipmentExtraReturnServiceTypeLasershipEnum",
    "ShipmentExtraReturnServiceTypeUPSEnum",
    "ShipmentExtraTypedDict",
    "ShipmentPaginatedList",
    "ShipmentPaginatedListTypedDict",
    "ShipmentStatus",
    "ShipmentTypedDict",
    "ShippoAccount",
    "ShippoAccountPaginatedList",
    "ShippoAccountPaginatedListTypedDict",
    "ShippoAccountTypedDict",
    "ShippoAccountUpdateRequest",
    "ShippoAccountUpdateRequestTypedDict",
    "SignatureConfirmation",
    "Track",
    "TrackTypedDict",
    "TrackingStatus",
    "TrackingStatusEnum",
    "TrackingStatusLocationBase",
    "TrackingStatusLocationBaseTypedDict",
    "TrackingStatusSubstatus",
    "TrackingStatusSubstatusTypedDict",
    "TrackingStatusTypedDict",
    "TracksRequest",
    "TracksRequestTypedDict",
    "Transaction",
    "TransactionCreateRequest",
    "TransactionCreateRequestTypedDict",
    "TransactionPaginatedList",
    "TransactionPaginatedListTypedDict",
    "TransactionStatusEnum",
    "TransactionTypedDict",
    "UPSConnectExistingOwnAccountParameters",
    "UPSConnectExistingOwnAccountParametersTypedDict",
    "UPSReferenceFields",
    "UPSReferenceFieldsTypedDict",
    "UserParcelTemplate",
    "UserParcelTemplateCreateRequest",
    "UserParcelTemplateCreateRequestTypedDict",
    "UserParcelTemplateList",
    "UserParcelTemplateListTypedDict",
    "UserParcelTemplateTypedDict",
    "UserParcelTemplateUpdateRequest",
    "UserParcelTemplateUpdateRequestTypedDict",
    "UserParcelTemplateWithCarrierTemplateCreateRequest",
    "UserParcelTemplateWithCarrierTemplateCreateRequestTypedDict",
    "UserParcelTemplateWithoutCarrierTemplateCreateRequest",
    "UserParcelTemplateWithoutCarrierTemplateCreateRequestTypedDict",
    "Webhook",
    "WebhookEventTypeEnum",
    "WebhookPaginatedList",
    "WebhookPaginatedListTypedDict",
    "WebhookPayload",
    "WebhookPayloadBatch",
    "WebhookPayloadBatchTypedDict",
    "WebhookPayloadTrack",
    "WebhookPayloadTrackTypedDict",
    "WebhookPayloadTransaction",
    "WebhookPayloadTransactionTypedDict",
    "WebhookPayloadTypedDict",
    "WebhookTypedDict",
    "WebhookUpdateRequest",
    "WebhookUpdateRequestTypedDict",
    "WeightUnitEnum",
]
