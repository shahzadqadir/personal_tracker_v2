from django.shortcuts import render
from django.utils import timezone
from track.models import Task, Objective, Goal, Sprint


def homepage(request):
    if request.user.is_authenticated: 
        user_objectives = Objective.objects.filter(owner=request.user)
        effort_done_per_objective = {}
        for objective in user_objectives:
            effort_done_per_objective[objective] = ((sum([
                task.effort_hours for task in objective.objective_tasks.all() if task.status=='complete'
            ]))/objective.effort_hours)*100
        context = {
            "tasks": Task.objects.filter(owner=request.user).filter(due_date__date=timezone.now()),
            
            "goals": Goal.objects.filter(owner=request.user)
                    .exclude(status__contains="complete")
                    .order_by('target_date'),

            "sprint": Sprint.objects.filter(owner=request.user).filter(status='inprogress').first(),

            "objectives": Objective.objects.filter(owner=request.user),
             
             "effort_done_per_objective": effort_done_per_objective,
             "test": {"name": "shahzad"}

        }        
        return render(request, 'pages/homepage.html', context)
    return render(request, 'pages/unauthorized.html')