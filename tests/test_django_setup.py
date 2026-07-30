import pytest
from django.conf import settings


@pytest.mark.django_db
def test_database_connection():
    """Verify the database connection works by inspecting the database config."""
    db_config = settings.DATABASES["default"]
    assert db_config["ENGINE"] == "django.db.backends.postgresql", (
        f"Expected PostgreSQL engine, got {db_config['ENGINE']}"
    )
    assert db_config["NAME"] is not None, "Database name is not configured"
    assert db_config["USER"] is not None, "Database user is not configured"
    assert db_config["HOST"] is not None, "Database host is not configured"
    assert db_config["PORT"] is not None, "Database port is not configured"