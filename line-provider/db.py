from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings
from logger import get_logger

Base = declarative_base()

engine = create_async_engine(settings.db.url)
session_factory = async_sessionmaker(bind=engine, autoflush=True, autocommit=False)

logger = get_logger(__name__)


async def get_session():
    async with session_factory() as session:
        try:
            yield session
        except Exception as e:
            logger.error("Exception %s. Rolling back session", e)
            await session.rollback()
        else:
            logger.debug("Commiting session")
            await session.commit()
