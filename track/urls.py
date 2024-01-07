from django.urls import path

from track.views import (
    goals_list, goal_detail,
    objectives_list, objective_detail,
    tasks_list
)

urlpatterns = [
    path("goals/", goals_list, name="goals_list"),    
    path("goals/<int:id>/", goal_detail, name="goal_detail"),
    path("objectives/", objectives_list, name="objectives_list"),
    path("objectives/<int:id>/", objective_detail, name="objective_detail"),
    path("tasks/", tasks_list, name="tasks_list"),
]