from shippo.models.components import ServiceGroup, ServiceLevel

import shippo


class TestServiceGroups:

    def test_service_groups(self, api: shippo.Shippo):
        service_groups = api.service_groups.list()

        assert service_groups is not None
        assert isinstance(service_groups, list)
        assert len(service_groups) > 0

        first_service_group = service_groups[0]
        assert first_service_group is not None
        assert isinstance(first_service_group, ServiceGroup)
        assert first_service_group.object_id is not None
        assert first_service_group.name is not None
        assert first_service_group.description is not None
        assert first_service_group.flat_rate_currency == 'USD'

        first_service_level = first_service_group.service_levels[0]
        assert first_service_level is not None
        assert isinstance(first_service_level, ServiceLevel)
        assert first_service_level.account_object_id is not None
        assert first_service_level.service_level_token is not None
