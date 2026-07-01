import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200

    data = res.get_json()
    assert data["status"] == "running"
    assert data["application"] == "devops-system-api"


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "healthy"


def test_system(client):
    res = client.get("/system")
    assert res.status_code == 200

    data = res.get_json()

    assert "hostname" in data
    assert "os" in data
    assert "os_version" in data
    assert "architecture" in data
    assert "python_version" in data


def test_app_info(client):
    res = client.get("/app-info")
    assert res.status_code == 200

    data = res.get_json()

    assert data["application"] == "devops-system-api"
    assert data["framework"] == "Flask"
    assert data["ci_platform"] == "GitHub Actions"
    assert data["containerized"] is True


def test_environment(client):
    res = client.get("/environment")
    assert res.status_code == 200

    data = res.get_json()

    assert "port" in data
    assert "hostname" in data


def test_uptime(client):
    res = client.get("/uptime")
    assert res.status_code == 200

    data = res.get_json()

    assert "uptime_seconds" in data
    assert data["uptime_seconds"] >= 0
