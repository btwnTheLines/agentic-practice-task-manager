"""
Behavioural tests for the task listing flow.

These tests validate user-visible behaviour through the Django test client:
rendering the list page, the empty state, displaying saved tasks in order,
the create-page link, and the complete create → redirect → list flow.
They intentionally avoid asserting on implementation details.
"""
from datetime import date

import pytest
from django.urls import reverse

from tasks.models import Task


@pytest.mark.django_db
class TestTaskListing:
    """User-visible behaviour of the /tasks/ page."""

    def test_list_page_renders(self, client):
        """
        Given a user visits the task list page
        When they request GET /tasks/
        Then the page loads successfully (200).
        """
        response = client.get(reverse("tasks:task_list"))
        assert response.status_code == 200

    def test_list_page_shows_empty_state_message(self, client):
        """
        Given there are no tasks in the database
        When a user requests GET /tasks/
        Then the page shows an empty-state message.
        """
        response = client.get(reverse("tasks:task_list"))
        assert response.status_code == 200
        assert b"No tasks yet." in response.content

    def test_list_page_displays_existing_tasks(self, client):
        """
        Given tasks exist in the database
        When a user requests GET /tasks/
        Then the page displays the titles of those tasks.
        """
        Task.objects.create(title="Write tests")
        Task.objects.create(title="Run CI")
        response = client.get(reverse("tasks:task_list"))
        assert response.status_code == 200
        assert b"Write tests" in response.content
        assert b"Run CI" in response.content

    def test_list_page_orders_tasks_newest_first(self, client):
        """
        Given multiple tasks exist in the database
        When a user requests GET /tasks/
        Then the tasks appear newest-first (by created_at).
        """
        first = Task.objects.create(title="First task")
        second = Task.objects.create(title="Second task")
        # Ensure deterministic ordering beyond sub-second timestamps.
        # created_at is auto_now_add; we rely on insertion order and
        # the model default ordering of -created_at.
        assert first.created_at <= second.created_at
        response = client.get(reverse("tasks:task_list"))
        first_pos = response.content.find(b"First task")
        second_pos = response.content.find(b"Second task")
        assert first_pos != -1 and second_pos != -1
        assert second_pos < first_pos

    def test_list_page_contains_link_to_create_task(self, client):
        """
        Given a user visits the task list page
        Then the page contains a link to create a new task.
        """
        response = client.get(reverse("tasks:task_list"))
        assert response.status_code == 200
        create_url = reverse("tasks:task_create")
        assert create_url.encode() in response.content

    def test_complete_flow_create_redirect_verify_in_list(self, client):
        """
        Given a user submits a valid task form
        When they POST /tasks/new/
        Then the response is a redirect (302)
        And the redirect target is the task list page
        And following the redirect displays the newly created task.
        """
        create_url = reverse("tasks:task_create")
        list_url = reverse("tasks:task_list")

        create_response = client.post(
            create_url,
            {
                "title": "Complete Stage 3C",
                "description": "Task listing with full flow.",
                "status": "pending",
                "due_date": date(2026, 8, 12),
            },
        )

        # 1. POST returns a redirect.
        assert create_response.status_code == 302

        # 2. The redirect target is the task list page.
        redirect_target = create_response["Location"]
        assert redirect_target == list_url

        # 3. Following the redirect displays the newly created task.
        list_response = client.get(redirect_target)
        assert list_response.status_code == 200
        assert b"Complete Stage 3C" in list_response.content
        assert Task.objects.filter(title="Complete Stage 3C").exists()