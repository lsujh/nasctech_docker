import pytest

from flask import Flask, request

from handler import handler
from main import app as flask_app


@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_app(app):
    assert app

def test_index(app, client):
    response = client.get('/start/')
    assert response.status_code == 200

def test_data(app, client):
    response = client.get("/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}")
    assert response.status_code == 200

def test_incorrect_data(app, client):
    response = client.get("/start/?={'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','}")
    assert response.status_code == 200

def test_handler():
    data = {'data' : [1, 2, 3, 4, 5], 'rule' : ['a','b','c','d','e','f']}
    result = handler(data)
    assert result == {'result': [5.1, 5.4, 5.9, 6.6, 7.5]}