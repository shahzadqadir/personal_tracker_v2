from django.urls import path

from track.views import (
    UnAuthorizedView,
    goals_list, goal_detail, goal_add, goal_update,
    GoalDeleteView,
    objectives_list, objective_detail, objective_add,
    objective_update, objective_delete, objectives_list_include_complete,
    TasksListView, TaskCreateView, TaskDetailView,
    TaskUpdateView,TaskDeleteView,
    SprintListView, SprintCreateView, SprintDetailView,
    SprintUpdateView, SprintDeleteView
)

urlpatterns = [    
    path("unauthorized/", UnAuthorizedView.as_view(), name="unauthorized"),
    # Goals
    path("goals/", goals_list, name="goals_list"),    
    path("goals/<int:id>/", goal_detail, name="goal_detail"),
    path("goals/<int:id>/update/", goal_update, name="goal_update"),
    path("goals/<int:pk>/delete/", GoalDeleteView.as_view(), name="goal_delete"),
    path("goals/add/", goal_add, name="goal_add"),
    # Objectives
    path("objectives/include_complete/", objectives_list_include_complete, name="objectives_list_include_complete"),
    path("objectives/", objectives_list, name="objectives_list"),    
    path("objectives/add/", objective_add, name="objective_add"),
    path("objectives/<int:id>/", objective_detail, name="objective_detail"),
    path("objectives/<int:id>/update/", objective_update, name="objective_update"),
    path("objectives/<int:id>/delete/", objective_delete, name="objective_delete"),
    # Tasks
    path("tasks/", TasksListView.as_view(), name="tasks_list"),
    path("tasks/add", TaskCreateView.as_view(), name="task_add"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    # Sprints
    path("sprints/", SprintListView.as_view(), name="sprints_list"),
    path("sprints/add/", SprintCreateView.as_view(), name="sprint_add"),
    path("sprints/<int:pk>/", SprintDetailView.as_view(), name="sprint_detail"),
    path("sprints/<int:pk>/update/", SprintUpdateView.as_view(), name="sprint_update"),
    path("sprints/<int:pk>/delete/", SprintDeleteView.as_view(), name="sprint_delete"),
]