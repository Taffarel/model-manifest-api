import pytest
from fastapi.testclient import TestClient
from src.presentation.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_generate_manifest_success(client):
    headers = {"Authorization": "Bearer token1"}
    payload = {
        "model_name": "testmodel",
        "model_source_url": "https://example.com/model",
        "replicas": 2,
        "memory": "100Mi",
    }
    response = client.post("/api/v1/manifest", json=payload, headers=headers)
    assert response.status_code == 200
    assert "manifest" in response.json()
    assert "kind: Model" in response.json()["manifest"]

@pytest.mark.asyncio
async def test_invalid_token(client):
    headers = {"Authorization": "Bearer invalid_token"}
    payload = {
        "model_name": "testmodel",
        "model_source_url": "https://example.com/model",
        "replicas": 2,
        "memory": "100Mi",
    }
    response = client.post("/api/v1/manifest", json=payload, headers=headers)
    assert response.status_code == 401