from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.database import engine
from app.models.base import Base
from app.routers import auth, client, ticket
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Create the database tables on startup.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(client.router, prefix="/clients", tags=["Clients"])
app.include_router(ticket.router, prefix="/tickets", tags=["Tickets"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
