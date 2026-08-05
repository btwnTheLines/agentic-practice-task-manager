"""
Behavioural tests for the task creation flow.

These tests validate user-visible behaviour through the Django test client:
rendering the form, creating a task via POST, redirecting after success,
and displaying validation errors. They intentionally avoid asserting on
implementation details such as query counts or model method internals.
"""
import pytest
from django.urls import reverse

from tasks.models import Task


@pytest.mark.django_db
class TestTaskCreation:
    """User-visible behaviour of the /tasks/new/ page."""

    def test_task_creation_page_renders(self, client):
        """
        Given a user visits the task creation page
        When they request GET /tasks/new/
        Then the page loads successfully (200).
        """
        response = client.get(reverse("tasks:task_create"))
        assert response.status_code == 200

    def test_valid_post_creates_task_and_redirects(self, client):
        """
        Given a user fills in a valid task form
        When they submit POST /tasks/new/
        Then the task is saved in the database
        And the user is redirected (302).
        """
        response = client.post(
            reverse("tasks:task_create"),
            {
                "title": "Write Sprint 3 report",
                "description": "Summarise what was delivered.",
                "status": "pending",
                "due_date": "2026-08-10",
            },
        )

        assert response.status_code == 302
        assert Task.objects.filter(title="Write Sprint 3 report").exists()

    def test_blank_title_redisplays_form_with_error(self, client):
        """
        Given a user submits the form without a title
        When they submit POST /tasks/new/
        Then the form is re-rendered (200)
        And a validation error is displayed on the page
        And no task is saved.
        """
        response = client.post(
            reverse("tasks:task_create"),
            {"title": "", "description": "", "status": "pending", "due_date": ""},
        )

        assert response.status_code == 200
        assert b"This field is required" in response.content
        assert Task.objects.count() == 0

    def test_invalid_post_redisplays_form(self, client):
        """
        Given a user submits the form with invalid data
        When they submit POST /tasks/new/ with a whitespace-only title
        Then the form is re-rendered (200)
        And no task is saved.
        """
        response = client.post(
            reverse("tasks:task_create"),
            {"title": "   ", "description": "", "status": "pending", "due_date": ""},
        )

        assert response.status_code == 200
        assert Task.objects.count() == 0