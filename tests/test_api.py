from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_good_price():
    r = client.get("/price?text=$1,299.99")
    assert r.status_code == 200
    assert r.json()["price"] == 1299.99


def test_bad_text():
    r = client.get("/price?text=Out%20of%20stock")
    assert r.status_code == 400


def test_missing_text():
    r = client.get("/price")
    assert r.status_code == 422


def test_plus_sign_in_url():
    r = client.get("/price?text=50.99+cad")
    assert r.status_code == 200