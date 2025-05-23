from pydantic import BaseModel, EmailStr
from typing import Optional

class ClientBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

class ClientOut(ClientBase):
    id: int
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True