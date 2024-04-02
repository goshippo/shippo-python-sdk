"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .trackingstatusenum import TrackingStatusEnum
from .trackingstatuslocationbase import TrackingStatusLocationBase
from .trackingstatussubstatus import TrackingStatusSubstatus
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from shippo import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackingStatus:
    r"""The latest tracking information of this shipment."""
    location: TrackingStatusLocationBase = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('location') }})
    r"""An object containing zip, city, state and country information of the tracking event."""
    object_created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    object_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_id') }})
    object_updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('object_updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    status: TrackingStatusEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    r"""Indicates the high level status of the shipment."""
    status_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Date and time when the carrier scanned this tracking event. This is displayed in UTC."""
    status_details: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_details') }})
    r"""The human-readable description of the status."""
    substatus: Optional[TrackingStatusSubstatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('substatus'), 'exclude': lambda f: f is None }})
    r"""A finer-grained classification of the tracking event."""
    

