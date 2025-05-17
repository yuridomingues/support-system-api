from fastapi import FastAPI
from app.api import client
from app.models.client import Base
from app.core.database import engine
from contextlib import asynccontextmanager

app = FastAPI()

app.include_router(client.router, prefix="/clients", tags=["clients"])

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create the database tables on startup.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(client.router, prefix="/clients", tags=["clients"])