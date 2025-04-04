from sqlalchemy import insert

from models.event import Event as EventModel
from serializers.event import Event
from repository.base_repository import BaseRepository


class EventRepository(BaseRepository):
    async def create(self, event: Event):
        query = insert(EventModel).values(**event.model_dump()).returning(EventModel)
        return await self.session.execute(query)
