import decimal
import uuid
from datetime import datetime

from common.enums import EventType
from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Numeric, UUID

from models.mixins import TimestampMixin


class Event(Base, TimestampMixin):
    id: Mapped[str] = mapped_column(type_=UUID, primary_key=True, default=uuid.uuid4)
    coefficient: Mapped[decimal.Decimal] = mapped_column(type_=Numeric(precision=6, scale=2))
    deadline: Mapped[datetime | None]
    state: Mapped[EventType] = mapped_column(default=EventType.NEW)
