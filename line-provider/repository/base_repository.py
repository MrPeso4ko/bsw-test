from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_session


class BaseRepository:
    def __init__(self, session: Annotated[AsyncSession, Depends(get_session)]) -> None:
        self.session = session
