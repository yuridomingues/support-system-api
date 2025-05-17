from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate
from typing import List
from fastapi import HTTPException

async def create_client(db: AsyncSession, 
client: ClientCreate):
    new_client = Client(**client.model_dump())
    db.add(new_client)
    await db.commit()
    await db.refresh(new_client)
    return new_client

async def get_clients(db: AsyncSession) -> List[Client]:
    result = await db.execute(select(Client))
    return result.scalars().all()

async def get_client_by_id(db: AsyncSession, client_id: int) -> Client:
    client = await db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

async def update_client(db: AsyncSession, 
    client_id: int, 
    client_data: ClientUpdate
    ) -> Client:
    client = await db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    for field, value in client_data.model_dump(exclude_unset=True).items():
        setattr(client, field, value)

    await db.commit()
    await db.refresh(client)
    return client

async def delete_client(db: AsyncSession, client_id: int):
    client = await db.get(Client, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    await db.delete(client)
    await db.commit()
    return {"detail": "Client deleted successfully"}