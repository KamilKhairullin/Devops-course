import requests
import pytest
from flask.testing import FlaskClient
from main import app

app.testing = True
client = app.test_client()

# @pytest.fixture
# def client():
#     pass

def test_acess():
    assert client.get("http://127.0.0.1:5000"), "Unreached."
