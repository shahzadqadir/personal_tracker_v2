from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from track.models import Task, Objective, Goal, Sprint
from os import path
import matplotlib.pyplot as plt


def homepage(request):

    
    if request.user.is_authenticated: 
        user_objectives = Objective.objects.filter(owner=request.user)
        effort_done_per_objective = {}
        for objective in user_objectives:
            effort_done_per_objective[objective] = ((sum([
                task.effort_hours for task in objective.objective_tasks.all() if task.status=='complete'
            ]))/objective.effort_hours)*100
        current_sprint = Sprint.objects.filter(owner=request.user).filter(status='inprogress').first()        
        
        context = {
            "tasks": Task.objects.filter(owner=request.user).filter(due_date__date=timezone.now()),

            
            "goals": Goal.objects.filter(owner=request.user)
                    .order_by('target_date'),

            "objectives": Objective.objects.filter(owner=request.user),
             
             "effort_done_per_objective": effort_done_per_objective,
             "test": {"name": "shahzad"}

        }

        if current_sprint != None:
            current_sprint_total_tasks = current_sprint.sprint_tasks.count()
            current_sprint_completed_tasks = current_sprint.sprint_tasks.filter(status="complete").count()
            current_sprint_percent_completed = current_sprint.get_percentage_completed


            # plot code starts here
            day_of_week = list(current_sprint.get_percentage_completed_by_date.keys())
            hours_worked = list(current_sprint.get_hours_worked_per_day.values())

            percentage_achieved = list(current_sprint.get_percentage_completed_by_date.values())
            print(percentage_achieved)
            print(current_sprint.get_percentage_completed_by_date)

            fig, ax1 = plt.subplots()
            ax1.plot(day_of_week, hours_worked, linestyle='--', markersize=10, color='royalblue', marker='D', label="Hours worked")
            ax1.set_xlabel("Day of Week")
            ax1.set_ylabel("Hours Worked", color='royalblue')
            ax2 = ax1.twinx()
            ax2.plot(day_of_week, percentage_achieved, color='#463A14', marker='o', label="Percentage Achieved")
            ax2.set_ylabel("Percentage Achieved", color='#463A14')
            ax1.set_facecolor("#FFC300")
            plt.legend()
            plt.grid(False)
            fig.suptitle(current_sprint.title)
            fig.savefig(path.join(settings.STATICFILES_DIRS[0], 'images/sprint_performance.png'))
            

            context["sprint"] = current_sprint
            context["sprint_task_count"] = current_sprint_total_tasks
            context["sprint_tasks_completed"] = current_sprint_completed_tasks
            context["sprint_percent_completed"] = current_sprint_percent_completed


        return render(request, 'pages/homepage.html', context)
    return render(request, 'pages/unauthorized.html')