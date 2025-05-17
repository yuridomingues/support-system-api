from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TicketStatus(str, Enum):
    ABERTO = "Aberto"
    EM_ANDAMENTO = "Em Andamento"
    FECHADO = "Fechado"

class TicketBase(BaseModel):
    category: str
    content: str
    status: TicketStatus = TicketStatus.ABERTO

class TicketCreate(TicketBase):
    client_id: int

class TicketUpdate(BaseModel):
    category: Optional[str] = None
    content: Optional[str] = None
    status: Optional[TicketStatus] = None

class TicketOut(TicketBase):
    id: int
    client_id: int

    class Config:
        from_attributes = True
