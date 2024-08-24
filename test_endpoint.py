import pytest
from main import app


@pytest.fixture
def curl():
    with app.test_client() as client:
        yield client


def test_hello_world(curl):
    response = curl.get('/api/hello')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}