"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from shippo import utils
from shippo._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from shippo.models import components, errors, operations
from typing import Optional

class TrackingStatus:
    r"""<p style=\\"text-align: center; background-color: #F2F3F4;\\"></br>
    If you purchased your shipping label through Shippo, you can also get all the tracking details of your Shipment 
    from the <a href=\"#tag/Transactions\">Transaction</a> object.
    </br></br></p>
    A tracking status of a package is an indication of current location of a package in the supply chain. For example,  sorting, warehousing, or out for delivery. Use the tracking status object to track the location of your shipments.

    When using your <a href=\"https://docs.goshippo.com/docs/guides_general/authentication/\">Test</a> token for tracking, you need to use Shippo's 
    predefined tokens for testing different tracking statuses. You can find more information in our 
    <a href=\"https://docs.goshippo.com/docs/tracking/tracking/\">Tracking tutorial</a> on how to do this, and what the 
    payloads look like.      
    <SchemaDefinition schemaRef=\"#/components/schemas/Track\"/>
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create(self, carrier: str, tracking_number: str, metadata: Optional[str] = None) -> components.Track:
        r"""Register a tracking webhook
        Registers a webhook that will send HTTP notifications to you when the status of your tracked package changes. For more details on creating a webhook, see our guides on <a href=\"https://docs.goshippo.com/docs/tracking/webhooks/\">Webhooks</a> and <a href=\"https://docs.goshippo.com/docs/tracking/tracking/\">Tracking</a>.
        """
        hook_ctx = HookContext(operation_id='CreateTrack', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = components.TracksRequest(
            carrier=carrier,
            tracking_number=tracking_number,
            metadata=metadata,
        )
        
        _globals = operations.CreateTrackGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/tracks', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, components.TracksRequest, "request", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Track])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    
    
    def get(self, tracking_number: str, carrier: str) -> components.Track:
        r"""Get a tracking status
        Returns the tracking status of a shipment using a carrier name and a tracking number.
        """
        hook_ctx = HookContext(operation_id='GetTrack', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetTrackRequest(
            tracking_number=tracking_number,
            carrier=carrier,
        )
        
        _globals = operations.GetTrackGlobals(
            shippo_api_version=self.sdk_configuration.globals.shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/tracks/{Carrier}/{TrackingNumber}', request, _globals)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request, _globals), **headers }
        query_params = { **utils.get_query_params(request, _globals), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.Track])
                return out
            
            content_type = http_res.headers.get('Content-Type')
            raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400 or http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

    

