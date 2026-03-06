from backend.app.core.config import Settings


def test_settings_reads_environment(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://dbuser:dbpass@db.example.com:5432/tasks")
    monkeypatch.setenv("JWT_SECRET_KEY", "test-secret")
    monkeypatch.setenv("ACCESS_TOKEN_EXPIRE_MINUTES", "45")

    settings = Settings()

    assert settings.database_url == "postgresql+psycopg://dbuser:dbpass@db.example.com:5432/tasks"
    assert settings.jwt_secret_key == "test-secret"
    assert settings.access_token_expire_minutes == 45


def test_settings_default_database_is_postgresql():
    settings = Settings()

    assert settings.database_url.startswith("postgresql+psycopg://")
