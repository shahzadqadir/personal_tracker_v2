from django.urls import path

from api import views

urlpatterns = [
    path("endpoints/", views.EndPointsList.as_view(), name="api_endpoints"),
    path("tasks/", views.TaskListAPIView.as_view(), name="api_tasks"),
    path("tasks/<int:pk>/", views.TaskDetailAPIView.as_view(), name="api_task_detail"),
    path("goals/", views.GoalListAPIView.as_view(), name="api_goals"),
    path("goals/<int:pk>/", views.GoalDetailAPIView.as_view(), name="api_goal_detail"),
    path("goals/<int:goal_pk>/objectives/", views.GoalObjectivesList.as_view(), name="api_goal_objectives_list"),
    path("objectives/", views.ObjectiveListAPIView.as_view(), name="api_objectives"),
    path("objectives/<int:pk>/", views.ObjectiveDetailAPIView.as_view(), name="api_objective_detail"),
    path("objectives/<int:objective_pk>/tasks/", views.ObjectiveTasksAPIView.as_view(), name="api_objective_tasks"),
    path("sprints/", views.SprintListCreateAPIView.as_view(), name="api_sprints"),
    path("sprints/<int:pk>/", views.SprintDetailAPIView.as_view(), name="api_sprint_detail"),
    path("sprints/<int:sprint_pk>/tasks/", views.SprintTasksListAPIView.as_view(), name="api_sprint_tasks"),
]