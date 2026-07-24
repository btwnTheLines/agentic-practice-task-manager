"""
Local development settings for taskmanager project.

Extends base settings with development-specific configuration.
"""
from .base import *  # noqa: F403, F401

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "taskmanager",
        "USER": "taskmanager",
        "PASSWORD": "taskmanager",
        "HOST": "localhost",
        "PORT": 5432,
    }
}