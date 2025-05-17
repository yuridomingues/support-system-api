from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.database import get_db
from app.schemas.ticket import TicketCreate, TicketOut, TicketUpdate
from app.controllers.ticket import (
    create_ticket,
    get_tickets,
    get_ticket_by_id,
    update_ticket,
    delete_ticket
)

router = APIRouter()

@router.post("/", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
async def create(ticket: TicketCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new support ticket.
    """
    return await create_ticket(db, ticket)

@router.get("/", response_model=List[TicketOut])
async def list_tickets(db: AsyncSession = Depends(get_db)):
    """
    List all support tickets.
    """
    return await get_tickets(db)

@router.get("/{ticket_id}", response_model=TicketOut)
async def get(ticket_id: int, db: AsyncSession = Depends(get_db)):
    """
    Get a support ticket by ID.
    """
    return await get_ticket_by_id(db, ticket_id)

@router.put("/{ticket_id}", response_model=TicketOut)
async def update(ticket_id: int, update_data: TicketUpdate, db: AsyncSession = Depends(get_db)):
    """
    Update a support ticket by ID.
    """
    return await update_ticket(db, ticket_id, update_data)

@router.delete("/{ticket_id}", status_code=status.HTTP_200_OK)
async def delete(ticket_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete a support ticket by ID.
    """
    return await delete_ticket(db, ticket_id)