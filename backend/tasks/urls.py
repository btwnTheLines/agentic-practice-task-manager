from django.urls import path

from .views import TaskCreateView

app_name = "tasks"

urlpatterns = [
    path("new/", TaskCreateView.as_view(), name="task_create"),
]