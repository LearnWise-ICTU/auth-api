import pytest
from httpx import AsyncClient




@pytest.mark.asyncio
async def test_user_registration(client_test: AsyncClient):
    user = {
        "name": {"first_name": "john", "last_name": "doe", "nickname": "johnny"},
        "email": "john@example.com",
        "password": "password",
    }
    response = await client_test.post("v1/users", json=user)
    assert response.status_code == 200

