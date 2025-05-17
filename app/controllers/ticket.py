from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate
from typing import List

async def create_ticket(db: AsyncSession, ticket: TicketCreate) -> Ticket:
    """
    Create a new ticket.
    """
    new_ticket = Ticket(**ticket.model_dump())
    db.add(new_ticket)
    await db.commit()
    await db.refresh(new_ticket)
    return new_ticket

async def get_tickets(db: AsyncSession) -> List[Ticket]:
    """
    Get all tickets.
    """
    result = await db.execute(select(Ticket))
    return result.scalars().all()

async def get_ticket_by_id(db: AsyncSession, ticket_id: int) -> Ticket:
    """
    Get a ticket by ID.
    """
    ticket = await db.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    return ticket

async def update_ticket(db: AsyncSession, ticket_id: int, ticket_data: TicketUpdate) -> Ticket:
    ticket = await db.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    
    for field, value in ticket_data.model_dump(exclude_unset=True).items():
        setattr(ticket, field, value)

    await db.commit()
    await db.refresh(ticket)
    return ticket

async def delete_ticket(db: AsyncSession, ticket_id: int):
    ticket = await db.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
    
    await db.delete(ticket)
    await db.commit()
    return {"detail": "Ticket deleted successfully"}