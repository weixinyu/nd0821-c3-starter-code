# test_main.py

import json
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_say_hello():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}
    
def test_post():
    data = json.dumps({"value": 10})
    r = client.post("/42?query=5", data=data)
    print(r.json())
    assert r.json()["path"] == 42
    assert r.json()["query"] == 5
    assert r.json()["body"] == {"value": 10}