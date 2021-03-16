import pytest

from flask import Flask, request

from handler import handler
from main import index, app


@pytest.fixture
def app():
    app = Flask(__name__)
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_handler(client):
    response = client.get('/start/')
    assert response.status_code == 200
