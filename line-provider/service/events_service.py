from typing import Annotated

from fastapi import Depends

from logger import get_logger
from models.event import Event
from repository.event_repository import EventRepository

logger = get_logger(__name__)


class EventsService:
    def __init__(self, event_repository: Annotated[EventRepository, Depends()]):
        self.event_repository = event_repository

    async def create_event(self, event: Event):
        try:
            await self.event_repository.create(event)
        except Exception as e:
            logger.error("Error occurred while creating event", exc_info=e)
            raise
