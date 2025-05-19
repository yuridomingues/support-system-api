from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.client import (
    create_client,
    delete_client,
    get_client_by_id,
    get_clients,
    update_client,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.schemas.client import ClientCreate, ClientOut, ClientUpdate

router = APIRouter()


@router.post("/", response_model=ClientOut)
async def create(
    client: ClientCreate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Create a new client.
    """
    return await create_client(db, client)


@router.get("/", response_model=List[ClientOut])
async def list_clients(
    db: AsyncSession = Depends(get_db),
    order_by: str = "id",
    order_dir: str = "asc",
    skip: int = 0,
    limit: int = 10,
    _: dict = Depends(get_current_user),
):
    """
    List all clients.
    """
    return await get_clients(db, order_by, order_dir, skip, limit)


@router.get("/{client_id}", response_model=ClientOut)
async def get_client(
    client_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Get a client by ID.
    """
    return await get_client_by_id(db, client_id)


@router.put("/{client_id}", response_model=ClientOut)
async def update(
    client_id: int,
    update_data: ClientUpdate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Update a client by ID.
    """
    return await update_client(db, client_id, update_data)


@router.delete("/{client_id}", status_code=status.HTTP_200_OK)
async def delete(
    client_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Delete a client by ID.
    """
    return await delete_client(db, client_id)
