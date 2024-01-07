from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from track.models import (
    Goal, Objective, Task, Sprint
)


@login_required
def goals_list(request):
    user_goals = Goal.objects.filter(owner=request.user)
    return render(request, "track/goals.html", {"goals": user_goals})


@login_required
def goal_detail(request, id):
    goal = get_object_or_404(Goal, id=id)
    if goal.owner != request.user:
        return render(request, "track/unauthorized.html")
    return render(request, "track/goal_detail.html", {"goal": goal})

@login_required
def objectives_list(request):
    objectives = Objective.objects.filter(owner=request.user)
    return render(request, "track/objectives.html", {"objectives": objectives})

@login_required
def objective_detail(request, id):
    objective = get_object_or_404(Objective, id=id)
    if objective.owner != request.user:
        return render(request, "track/unauthorized.html")
    return render(request, "track/objective_detail.html", {"objective": objective})

@login_required
def tasks_list(request):
    tasks = Task.objects.filter(owner=request.user)
    return render(request, "track/tasks.html", {"tasks": tasks})



