from fastapi import APIRouter
from serializers.event import Event

events_router = APIRouter(prefix="/events", tags=["Events"])


@events_router.post("")
async def create_event(event: Event, events_service: Annotated[EventsService, Depends()]) -> Event:
    return events_service.create(event)
