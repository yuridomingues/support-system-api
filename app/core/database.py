from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)

from typing import AsyncGenerator

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    db = async_session()
    try:
        yield db
    finally:
        await db.close()