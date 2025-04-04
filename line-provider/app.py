from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.v1.root import v1_router


@asynccontextmanager
async def lifespan(app):
    yield


class App(FastAPI):
    def __init__(self):
        super().__init__(lifespan=lifespan, name="Line Provider")

        self.include_router(v1_router)