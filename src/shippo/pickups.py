"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .basesdk import BaseSDK
from shippo._hooks import HookContext
from shippo.models import components, errors, operations
from shippo.types import BaseModel
import shippo.utils as utils
from typing import Optional, Union

class Pickups(BaseSDK):
    r"""A pickup is when you schedule a carrier to collect a package for delivery.
    Use Shippo’s pickups endpoint to schedule pickups with USPS and DHL Express for eligible shipments that you have already created.
    <SchemaDefinition schemaRef=\"#/components/schemas/Pickup\"/>
    """
    
    
    def create(
        self, *,
        request: Union[components.PickupBase, components.PickupBaseTypedDict],
        server_url: Optional[str] = None,
    ) -> components.Pickup:
        r"""Create a pickup

        Creates a pickup object. This request is for a carrier to come to a specified location to take a package for shipping.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = components.PickupBase(
            request=utils.unmarshal(request, components.PickupBase) if not isinstance(request, BaseModel) else request,
        )
        
        req = self.build_request(
            method="POST",
            path="/pickups",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.CreatePickupGlobals(
                shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", components.PickupBase),
        )
        
        http_res = self.do_request(
            hook_ctx=HookContext(operation_id="CreatePickup", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","4XX","5XX"],
        )
        
        
        if http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get("Content-Type") or "", "application/json"):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Pickup])
                return out
            
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"unknown content-type received: {content_type}", http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError("unknown status code received", http_res.status_code, http_res.text, http_res)
    
    
    async def create_async(
        self, *,
        request: Union[components.PickupBase, components.PickupBaseTypedDict],
        server_url: Optional[str] = None,
    ) -> components.Pickup:
        r"""Create a pickup

        Creates a pickup object. This request is for a carrier to come to a specified location to take a package for shipping.

        :param request: The request object to send.
        :param server_url: Override the default server URL for this method
        """
        base_url = None
        url_variables = None
        if server_url is not None:
            base_url = server_url
        
        request = components.PickupBase(
            request=utils.unmarshal(request, components.PickupBase) if not isinstance(request, BaseModel) else request,
        )
        
        req = self.build_request(
            method="POST",
            path="/pickups",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            _globals=operations.CreatePickupGlobals(
                shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
            ),
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(request, False, False, "json", components.PickupBase),
        )
        
        http_res = await self.do_request_async(
            hook_ctx=HookContext(operation_id="CreatePickup", oauth2_scopes=[], security_source=self.sdk_configuration.security),
            request=req,
            error_status_codes=["400","4XX","5XX"],
        )
        
        
        if http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get("Content-Type") or "", "application/json"):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Pickup])
                return out
            
            content_type = http_res.headers.get("Content-Type")
            raise errors.SDKError(f"unknown content-type received: {content_type}", http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError("API error occurred", http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError("unknown status code received", http_res.status_code, http_res.text, http_res)
    
