import pytest
from httpx import AsyncClient

async def get_auth_headers(client):
    res = await client.post(
        "/auth/token",
        data={"username": "admin", "password": "1234"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

@pytest.mark.asyncio
async def test_create_client(client):
    headers = await get_auth_headers(client)
    res = await client.post("/clients/", json={
        "name": "Yuri",
        "email": "yuri@example.com",
        "phone": "35999999999"
    }, headers=headers)

    assert res.status_code == 201
    data = res.json()
    assert data["name"] == "Yuri"
    assert data["email"] == "yuri@example.com"

@pytest.mark.asyncio
async def test_list_clients(client):
    headers = await get_auth_headers(client)
    res = await client.get("/clients/", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert isinstance(data, list)
    assert any(c["email"] == "yuri@example.com" for c in data)

@pytest.mark.asyncio
async def test_update_client(client):
    headers = await get_auth_headers(client)
    create_res = await client.post("/clients/", json={
        "name": "Ana",
        "email": "ana@example.com"
    }, headers=headers)
    print("CREATE RESPONSE:", create_res.json()) 
    client_id = create_res.json()["id"]

    res = await client.put(f"/clients/{client_id}", json={
        "name": "Ana Atualizada",
        "email": "ana@example.com",
        "phone": "3522334455"
    }, headers=headers)
    assert res.status_code == 200
    updated = res.json()
    assert updated["name"] == "Ana Atualizada"

@pytest.mark.asyncio
async def test_delete_client(client):
    headers = await get_auth_headers(client)
    create_res = await client.post("/clients/", json={
        "name": "Delete Me",
        "email": "deleteme@example.com"
    }, headers=headers)
    client_id = create_res.json()["id"]

    delete_res = await client.delete(f"/clients/{client_id}", headers=headers)
    assert delete_res.status_code == 204

    list_res = await client.get("/clients/", headers=headers)
    emails = [c["email"] for c in list_res.json()]
    assert "deleteme@example.com" not in emails
