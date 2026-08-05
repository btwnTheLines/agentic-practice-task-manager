from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import TaskForm


class TaskCreateView(CreateView):
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task_create")