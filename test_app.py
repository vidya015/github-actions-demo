import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_health(client):
    r = client.get('/health')
    assert r.status_code == 200
    assert r.get_json()['status'] == 'ok'

def test_square(client):
    r = client.get('/square/5')
    assert r.get_json()['result'] == 25

def test_greet(client):
    r = client.get('/greet/SGU')
    assert 'Hello, SGU!' in r.get_json()['message']