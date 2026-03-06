import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

# Ensure app settings load a dedicated SQLite database for tests.
os.environ["DATABASE_URL"] = "sqlite:///./test_task_manager.db"

from app.db.session import engine
from app.main import app
from app.models import Base


@pytest.fixture(autouse=True)
def test_db() -> Generator[None, None, None]:
    """Create a clean test database for each test and tear it down afterwards."""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    try:
        yield
    finally:
        Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client
