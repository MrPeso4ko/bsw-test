from fastapi import APIRouter

from api.v1.event import events_router

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(events_router)