"""공통 학습 모델을 사용하는 FastAPI 계약 테스트."""
import json
from pathlib import Path

from fastapi.testclient import TestClient

from week4.main import app

client = TestClient(app)
SAMPLE = json.loads(Path(__file__).with_name("sample_request.json").read_text())


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}


def test_predict():
    response = client.post("/predict", json=SAMPLE)
    assert response.status_code == 200
    result = response.json()
    assert set(result) == {"churn", "churn_probability"}
    assert type(result["churn"]) is int
    assert result["churn"] in (0, 1)
    assert isinstance(result["churn_probability"], float)
    assert 0 <= result["churn_probability"] <= 1


def test_missing_required_field():
    payload = SAMPLE.copy()
    payload.pop("tenure")
    response = client.post("/predict", json=payload)
    assert response.status_code == 422
    assert any(error["loc"] == ["body", "tenure"] for error in response.json()["detail"])
