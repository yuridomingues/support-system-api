import pytest


@pytest.mark.asyncio
async def test_login_success(client):
    res = await client.post(
        "auth/token",
        data={"username": "admin", "password": "1234"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert res.status_code == 200
    assert "access_token" in res.json()


@pytest.mark.asyncio
async def test_login_failure(client):
    res = await client.post(
        "auth/token",
        data={"username": "admin", "password": "wrong"},
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    assert res.status_code == 401
    assert res.json()["detail"] == "Usuário ou senha inválidos"
