import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from ..main import app
from ..database import Base

@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("sqlite:///./test.db")
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    yield TestingSessionLocal()

    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_db):
    with TestClient(app) as client:
        yield client


def test_create_product(client):
    response = client.post("/products/", json={"name": "Test Product", "description": "A test product", "price": 10.0,
                                               "quantity": 100})

    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
