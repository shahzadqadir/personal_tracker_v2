from django.urls import path

from api.views import (
    TaskListAPIView, TaskDetailAPIView,
    GoalListAPIView, ObjectiveListAPIView,
    SprintListAPIView, GoalDetailAPIView
)

urlpatterns = [
    path("tasks/", TaskListAPIView.as_view(), name="api_tasks"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="api_task_detail"),
    path("goals/", GoalListAPIView.as_view(), name="api_goals"),
    path("goals/<int:pk>/", GoalDetailAPIView.as_view(), name="api_goal_detail"),
    path("objectives/", ObjectiveListAPIView.as_view(), name="api_objectives"),
    path("sprints/", SprintListAPIView.as_view(), name="api_sprints"),
]