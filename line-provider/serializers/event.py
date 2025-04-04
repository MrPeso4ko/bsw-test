import decimal

from pydantic import BaseModel, ConfigDict

from common.enums import EventType


class Event(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    event_id: str
    coefficient: decimal.Decimal
    deadline: int | None
    state: EventType
