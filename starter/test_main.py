# test_main.py

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_say_hello():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"greeting": "Hello World!"}


def test_predict_1():
    data = '{"age": 65, "workclass": "Private",\
        "fnlgt": 153522, "education": "HS-grad",\
        "education-num": 9, "marital-status": "Widowed",\
        "occupation": "Other-service", "relationship": "Unmarried",\
        "race": "White", "sex": "Female", "capital-gain": 0,\
        "capital-loss": 0, "hours-per-week": 17,\
        "native-country": "United-States"}'
    r = client.post("/predict", data=data)
    assert r.status_code == 200
    print(r.json())
    assert r.json()["result"] == '<=50K'


def test_predict_2():
    data = '{"age": 58, "workclass": "Federal-gov",\
        "fnlgt": 72998, "education": "11th", "education-num": 7,\
        "marital-status": "Divorced", "occupation": "Craft-repair",\
        "relationship": "Not-in-family", "race": "Black",\
        "sex": "Female", "capital-gain": 14084, "capital-loss": 0,\
        "hours-per-week": 40, "native-country": "United-States"}'
    r = client.post("/predict", data=data)
    assert r.status_code == 200
    print(r.json())
    assert r.json()["result"] == '>50K'
