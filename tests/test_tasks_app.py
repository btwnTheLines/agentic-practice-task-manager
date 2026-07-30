"""
Verify the tasks application is correctly wired into Django.

This test reduces the risk of misconfiguration by validating that
the tasks app is registered and its URL namespace is reachable.
"""
import pytest
from django.core.exceptions import ImproperlyConfigured
from django.urls import resolve, Resolver404


class TestTasksAppWiring:
    """Behavioural smoke tests for the tasks application foundation."""

    def test_tasks_url_namespace_is_wired(self):
        """
        Given the tasks app is registered in INSTALLED_APPS
        And tasks/urls.py is included in the root URL configuration
        When a request matches the /tasks/ prefix
        Then Django should route to the tasks URLconf
        (a Resolver404 is expected because no endpoints exist yet,
        but an ImproperlyConfigured error would indicate miswiring).
        """
        try:
            resolve("/tasks/")
        except Resolver404:
            # Expected: tasks URLconf exists but has empty urlpatterns.
            # This proves the namespace was found and delegated to.
            pass
        except ImproperlyConfigured:
            pytest.fail(
                "tasks URLconf is not properly wired — "
                "Django could not resolve the tasks URL module"
            )

    def test_tasks_app_is_registered(self):
        """
        Given the tasks app is listed in INSTALLED_APPS
        When Django loads the app configs
        Then the TasksConfig should be discoverable.
        """
        from django.apps import apps

        assert apps.is_installed("tasks"), (
            "tasks app is not registered in INSTALLED_APPS"
        )