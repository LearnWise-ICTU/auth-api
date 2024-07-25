import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app import app


@pytest.fixture
async def client_test():
    print("Setting up client_test fixture")
    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test", follow_redirects=True) as client:
            yield client
    print("Tearing down client_test fixture")