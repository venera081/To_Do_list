from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('items/', TaskListCreateView.as_view()),
    path('items/<int:pk>/', TaskDetailView.as_view()),
]
