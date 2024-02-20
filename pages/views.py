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
        current_sprint = Sprint.objects.filter(owner=request.user).filter(status='inprogress').first()
        current_sprint_total_tasks = current_sprint.sprint_tasks.count()
        current_sprint_completed_tasks = current_sprint.sprint_tasks.filter(status="complete").count()
        current_sprint_percent_completed = round((current_sprint_completed_tasks/current_sprint_total_tasks)*100, 2)

        context = {
            "tasks": Task.objects.filter(owner=request.user).filter(due_date__date=timezone.now()),

            
            "goals": Goal.objects.filter(owner=request.user)
                    .exclude(status__contains="complete")
                    .order_by('target_date'),

            "sprint": current_sprint,
            "sprint_task_count": current_sprint_total_tasks,
            "sprint_tasks_completed": current_sprint_completed_tasks,
            "sprint_percent_completed": current_sprint_percent_completed,

            "objectives": Objective.objects.filter(owner=request.user),
             
             "effort_done_per_objective": effort_done_per_objective,
             "test": {"name": "shahzad"}

        }        
        return render(request, 'pages/homepage.html', context)
    return render(request, 'pages/unauthorized.html')