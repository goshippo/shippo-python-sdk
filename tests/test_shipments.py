import re
from typing import List

import shippo
from shippo.models.components import ShipmentPaginatedList, Shipment
from shippo.models.operations import ListShipmentsRequest


class TestShipments:

    def test_list_all_shipments(self, api: shippo.Shippo):

        response = api.shipments.list(request=ListShipmentsRequest())

        assert response is not None
        assert response.results is not None
        assert isinstance(response, ShipmentPaginatedList)

        assert_shipment_results(response.results)

    def test_list_all_shipments_pagination(self, api: shippo.Shippo):
        response = api.shipments.list(request=ListShipmentsRequest(page=1, results=2))

        assert response is not None
        assert response.results is not None
        assert isinstance(response, ShipmentPaginatedList)

        assert_shipment_results(response.results)

        if response.next is not None:
            page_token_match = re.search(r"page_token=([^&]+)", response.next)
            assert page_token_match is not None

            page_token = page_token_match.group(1)
            secondResponse = api.shipments.list(
                request=ListShipmentsRequest(page_token=page_token, page=2, results=2)
            )
            assert secondResponse is not None
            assert secondResponse.results is not None
            assert isinstance(response, ShipmentPaginatedList)
            assert_shipment_results(secondResponse.results)


def assert_shipment_results(results: List[Shipment]):
    assert isinstance(results, list)
    if len(results) > 0:
        for result in results:
            assert isinstance(result, Shipment)
            assert result.object_id is not None
            assert result.object_id is not None
            assert result.address_from is not None
            assert result.address_to is not None
