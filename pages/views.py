from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from track.models import Task, Objective, Goal, Sprint
from os import path
import matplotlib.pyplot as plt
import datetime


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
            ax1.bar(day_of_week, hours_worked, label="Hours worked", color="#c9abb3")
            ax1.set_xlabel("Day of Week")
            ax1.set_ylabel("Hours Worked", color='#c9abb3')
            ax2 = ax1.twinx()
            ax2.plot(day_of_week, percentage_achieved, label="Percentage Achieved", marker='o', color="green")
            ax2.set_ylabel("Percentage Achieved", color='green')
            plt.legend()
            plt.grid(False)
            fig.suptitle(current_sprint.title)
            fig.savefig(path.join(settings.STATICFILES_DIRS[0], 'images/sprint_performance.png'))
            
            recent_sprints = Sprint.objects.order_by("-start_date")[:6]
            recent_sprint_ids = ["WK"+str(sprint.id+1) for sprint in recent_sprints]
            recent_sprints_percent_completed = [sprint.get_percentage_completed for sprint in recent_sprints]
            f1 = plt.figure()
            cols = []
            for percentage in recent_sprints_percent_completed:
                print(percentage)
                if percentage >= 95:
                    cols.append('#006400')
                elif percentage > 90 and percentage < 95:
                    cols.append('#708238')
                elif percentage > 60 and percentage < 90:
                    cols.append('#b2ac88')
                else:
                    cols.append('#dc143c')
            plt.bar(recent_sprint_ids, recent_sprints_percent_completed, color=cols)
            plt.bar_label(plt.gca().containers[0])
            plt.xlabel("Sprint")
            plt.ylabel("Percentage Achieved")
            # if (datetime.datetime.now().date() - recent_sprints[0].end_date) > 30:
            #     f1.savefig(path.join(settings.STATICFILES_DIRS[0], 'images/recent_sprints_performance_archive.png'))
            # else:
            #     f1.savefig(path.join(settings.STATICFILES_DIRS[0], 'images/recent_sprints_performance.png'))

            context["sprint"] = current_sprint
            context["sprint_task_count"] = current_sprint_total_tasks
            context["sprint_tasks_completed"] = current_sprint_completed_tasks
            context["sprint_percent_completed"] = current_sprint_percent_completed


        return render(request, 'pages/homepage.html', context)
    return render(request, 'pages/unauthorized.html')