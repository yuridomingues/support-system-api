import pytest
import uuid
from httpx import AsyncClient
from tests.test_clients import get_auth_headers


async def create_sample_client(client, headers):
    unique_email = f"cliente_{uuid.uuid4().hex[:8]}@example.com"
    res = await client.post("/clients/", json={
        "name": "Cliente Ticket",
        "email": unique_email,
        "phone": "999999999"
    }, headers=headers)
    return res.json()["id"]

@pytest.mark.asyncio
async def test_create_ticket(client: AsyncClient):
    headers = await get_auth_headers(client)
    client_id = await create_sample_client(client, headers)

    res = await client.post("/tickets/", json={
        "category": "Login",
        "content": "Não consigo acessar o sistema",
        "client_id": client_id
    }, headers=headers)

    assert res.status_code == 201
    data = res.json()
    assert data["category"] == "Login"
    assert data["client_id"] == client_id


@pytest.mark.asyncio
async def test_list_tickets(client: AsyncClient):
    headers = await get_auth_headers(client)
    res = await client.get("/tickets/", headers=headers)
    assert res.status_code == 200
    assert isinstance(res.json(), list)


@pytest.mark.asyncio
async def test_update_ticket(client: AsyncClient):
    headers = await get_auth_headers(client)
    client_id = await create_sample_client(client, headers)

    create_res = await client.post("/tickets/", json={
        "category": "Rede",
        "content": "Sem acesso à internet",
        "client_id": client_id
    }, headers=headers)
    ticket_id = create_res.json()["id"]

    update_res = await client.put(f"/tickets/{ticket_id}", json={
        "status": "Fechado",
        "content": "Problema resolvido"
    }, headers=headers)

    assert update_res.status_code == 200
    assert update_res.json()["status"] == "Fechado"


@pytest.mark.asyncio
async def test_delete_ticket(client: AsyncClient):
    headers = await get_auth_headers(client)
    client_id = await create_sample_client(client, headers)

    create_res = await client.post("/tickets/", json={
        "category": "Exclusão",
        "content": "Remover este ticket",
        "client_id": client_id
    }, headers=headers)
    ticket_id = create_res.json()["id"]

    delete_res = await client.delete(f"/tickets/{ticket_id}", headers=headers)
    assert delete_res.status_code == 204
