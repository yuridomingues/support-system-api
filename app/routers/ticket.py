from typing import List

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.controllers.ticket import (
    create_ticket,
    delete_ticket,
    get_ticket_by_id,
    get_tickets,
    update_ticket,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.schemas.ticket import TicketCreate, TicketOut, TicketUpdate

router = APIRouter()


@router.post("/", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
async def create(
    ticket: TicketCreate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Create a new support ticket.
    """
    return await create_ticket(db, ticket)


@router.get("/", response_model=List[TicketOut], status_code=status.HTTP_200_OK)
async def list_tickets(
    db: AsyncSession = Depends(get_db),
    order_by: str = "id",
    order_dir: str = "asc",
    skip: int = 0,
    limit: int = 10,
    _: dict = Depends(get_current_user),
):
    """
    List all support tickets.
    """
    return await get_tickets(db, order_by, order_dir, skip, limit)


@router.get("/{ticket_id}", response_model=TicketOut, status_code=status.HTTP_200_OK)
async def get(
    ticket_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Get a support ticket by ID.
    """
    return await get_ticket_by_id(db, ticket_id)


@router.put("/{ticket_id}", response_model=TicketOut, status_code=status.HTTP_200_OK)
async def update(
    ticket_id: int,
    update_data: TicketUpdate,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Update a support ticket by ID.
    """
    return await update_ticket(db, ticket_id, update_data)


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    ticket_id: int,
    db: AsyncSession = Depends(get_db),
    _: dict = Depends(get_current_user),
):
    """
    Delete a support ticket by ID.
    """
    await delete_ticket(db, ticket_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)