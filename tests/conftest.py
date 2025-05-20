import os
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.core.database import get_db
from app.models.base import Base

TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine_test = create_async_engine(TEST_DATABASE_URL, echo=False)
async_session_test = sessionmaker(
    bind=engine_test,
    expire_on_commit=False,
    class_=AsyncSession,
)

@pytest_asyncio.fixture(scope="session", autouse=True)
async def prepare_database():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

@pytest_asyncio.fixture
async def db_session():
    async with async_session_test() as session:
        yield session

@pytest_asyncio.fixture
async def client(db_session):
    app.dependency_overrides[get_db] = lambda: db_session
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
