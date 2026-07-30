"""
Local development settings for taskmanager project.

Extends base settings with development-specific configuration.
Reads database connection parameters from environment variables
with sensible defaults for local development without Docker.
"""
import os

from .base import *  # noqa: F403, F401

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "taskmanager"),
        "USER": os.environ.get("POSTGRES_USER", "taskmanager"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "taskmanager"),
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}
