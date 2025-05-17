from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.api import client, ticket, auth
from app.core.database import engine
from app.models.base import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create the database tables on startup.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(client.router, prefix="/clients", tags=["Clients"])
app.include_router(ticket.router, prefix="/tickets", tags=["Tickets"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
