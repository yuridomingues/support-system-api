from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.client import ClientCreate, ClientOut, ClientUpdate
from app.controllers.client import (
    create_client,
    get_clients,
    get_client_by_id,
    update_client,
    delete_client
)
from app.core.security import get_current_user
from typing import List

router = APIRouter()

@router.post("/", response_model=ClientOut)
async def create(client: ClientCreate, db: AsyncSession = Depends(get_db), user=Depends(get_current_user)):
    """
    Create a new client.
    """
    return await create_client(db, client)

@router.get("/", response_model=List[ClientOut])
async def list_clients(db: AsyncSession = Depends(get_db)):
    """
    List all clients.
    """
    return await get_clients(db)

@router.get("/{client_id}", response_model=ClientOut)
async def get_client(client_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get a client by ID.
    """
    return await get_client_by_id(db, client_id)

@router.put("/{client_id}", response_model=ClientOut)
async def update(client_id: int, update_data: ClientUpdate, db: AsyncSession = Depends(get_db)):
    """
    Update a client by ID.
    """
    return await update_client(db, client_id, update_data)

@router.delete("/{client_id}", status_code=status.HTTP_200_OK)
async def delete(client_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a client by ID.
    """
    return await delete_client(db, client_id)
