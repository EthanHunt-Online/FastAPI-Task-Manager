import pytest

from app.config import Settings


def test_settings_reads_environment(monkeypatch):
    monkeypatch.setenv("SECRET_KEY", "test-secret")
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "45")
    monkeypatch.setenv("DATABASE_URL", "sqlite:///./test.db")

    settings = Settings()

    assert settings.secret_key == "test-secret"
    assert settings.access_token_expire_minutes == 45
    assert settings.database_url == "sqlite:///./test.db"


def test_secret_key_required(monkeypatch):
    monkeypatch.delenv("SECRET_KEY", raising=False)

    with pytest.raises(Exception):
        Settings()
