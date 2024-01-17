from django.shortcuts import render
from django.utils import timezone
from track.models import Task, Objective, Goal, Sprint


def homepage(request):
    if request.user.is_authenticated: 
        context = {
            "tasks": Task.objects.filter(owner=request.user),
            "goals": Goal.objects.filter(owner=request.user)
                    .exclude(status__contains="complete")
                    .order_by('target_date'),

            "sprint": Sprint.objects.filter(owner=request.user).first(), 

        }        
        return render(request, 'pages/homepage.html', context)
    return render(request, 'pages/unauthorized.html')