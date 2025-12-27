from django.urls import path
from .views import TaskListCreateView, TaskDetailView

taskurlpatterns = [
    path('task/', TaskListCreateView.as_view()),
    path('task/<int:pk>/', TaskDetailView.as_view()),
]
