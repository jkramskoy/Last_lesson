import os
import pytest
from main import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"
    client = app.test_client()

    cleanup()

    db.create_all()

    yield client

def cleanup():
    db.drop_all()

def test_index_not_logged_in(client):
    response = client.get("/")    # get request to our '/' path
    assert b'Enter your name' in response.data

def test_index_logged_in(client):
    client.post("/login",data= {"user-name":"Test User",
                                "user-email":"test@user.com",
                                "user-password":"123456"},
                follow_redirects=True)
    response = client.get("/")    # get request to our '/' path
    assert b'Enter your guess' in response.data