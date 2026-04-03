"""API Tests — generados por ATLAS CORE — gestion-de-pacientes-para-clinica-dental-con-citas-y"""
import random
import pytest
from fastapi.testclient import TestClient
from main import app
from database import init_db

init_db()
client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_docs():
    r = client.get("/docs")
    assert r.status_code == 200


def test_auth_login_requires_credentials():
    r = client.post("/auth/login", json={"email": "x@x.com", "password": "x"})
    assert r.status_code in [401, 422]


def test_auth_me_requires_token():
    r = client.get("/auth/me")
    assert r.status_code == 401


def test_register_and_login():
    email    = f"test{random.randint(10000,99999)}@test.com"
    username = f"user{random.randint(10000,99999)}"

    r = client.post("/auth/register", json={"email": email, "username": username, "password": "testpass123"})
    assert r.status_code == 200, f"Register failed: {r.json()}"

    r = client.post("/auth/login", json={"email": email, "password": "testpass123"})
    assert r.status_code == 200, f"Login failed: {r.json()}"
    assert "access_token" in r.json()


def test_pacientes_require_auth():
    r = client.get("/items/")  # Paciente
    assert r.status_code == 401


def test_citas_require_auth():
    r = client.get("/items/citas/")  # Cita
    assert r.status_code == 401


def test_tratamientos_require_auth():
    r = client.get("/items/tratamientos/")  # Tratamiento
    assert r.status_code == 401
