from typing import Any
from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from django.views.generic import (
    DeleteView, ListView, CreateView,
    TemplateView, UpdateView, DetailView
)
from django.contrib.auth.mixins import LoginRequiredMixin

from track import forms
from track import models


from track.models import (
    Goal, Objective, Task, Sprint
)


# Goals

@login_required
def goals_list(request):
    form = forms.SearchForm()
    user_goals = Goal.objects.filter(owner=request.user).order_by("-target_date")

    

    if request.method == "POST":
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            user_goals = user_goals.filter(description__icontains=search)
    return render(request, "track/goals/goals.html", {"goals": user_goals, "form": form})


@login_required
def goal_detail(request, id):
    goal = get_object_or_404(Goal, id=id)
    if goal.owner != request.user:
        return render(request, "track/unauthorized.html")
    return render(request, "track/goals/goal_detail.html", {"goal": goal})


@login_required
def goal_add(request):
    form = forms.GoalsForm()
    if request.method == "POST":
        form = forms.GoalsForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()        
            return redirect("goals_list")
    return render(request, "track/goals/goal_add.html", {"form": form})


@login_required
def goal_update(request, id):
    goal = Goal.objects.get(id=id)
    if goal.owner != request.user:
        return redirect(reverse_lazy("unauthorized"))
    if request.method == "POST":
        form = forms.GoalsForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals_list")
    else:
        form = forms.GoalsForm(instance=goal)
        return render(request, "track/goals/goal_edit.html", {"form": form})
  

class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    success_url = reverse_lazy("goals_list")
    template_name = "track/goals/goal_delete.html"

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return redirect(reverse_lazy("unauthorized"))
        return super().post(self.request, *args, **kwargs)
    

# Objectives

@login_required
def objectives_list(request):
    
    objectives = Objective.objects.filter(owner=request.user).exclude(status="complete")
    form = forms.SearchForm()
    if request.method == "POST":
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            objectives = objectives.filter(description__icontains=search)
            
    return render(request, "track/objectives/objectives.html", 
                  {
                      "objectives": objectives,
                      "include_completed": False,
                      "form": form,
                   })

def objectives_list_include_complete(request):
    objectives = Objective.objects.filter(owner=request.user).order_by("-status")
    return render(request, "track/objectives/objectives.html", 
                  {
                      "objectives": objectives,
                      "include_completed": True,
                   })

@login_required
def objective_detail(request, id):
    objective = get_object_or_404(Objective, id=id)
    if objective.owner != request.user:
        return render(request, "track/unauthorized.html")
    return render(request, "track/objectives/objective_detail.html", {"objective": objective})


@login_required
def objective_add(request):
    form = forms.ObjectivesForm()
    if request.method == "POST":
        form = forms.ObjectivesForm(request.POST)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect("objectives_list")
    return render(request, "track/objectives/objective_add.html", {"form": form})


@login_required
def objective_update(request, id):
    objective = Objective.objects.get(id=id)
    if objective.owner != request.user:
        return redirect("goals_list")
    if request.method == "POST":
        form = forms.ObjectivesForm(request.POST, instance=objective)
        if form.is_valid():
            form.save()
            return redirect("objectives_list")
    else:
        form = forms.ObjectivesForm(instance=objective)
        return render(request, "track/objectives/objective_edit.html", {"form": form})
    

@login_required
def objective_delete(request, id):
    objective = Objective.objects.get(id=id)
    if objective.owner != request.user:
        return redirect(reverse_lazy("unauthorized"))
    if request.method == "POST":
        objective.delete()
        return redirect("objectives_list")
    else:
        return render(request, "track/objectives/objective_delete.html")
    

@login_required
def objectives_search(request):
    pass

# Unauthorized.


class UnAuthorizedView(TemplateView):
    template_name = "track/unauthorized.html"

# Tasks
 

class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "track/tasks/tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(TasksListView, self).get_context_data(**kwargs)
        context["form"] = forms.SearchForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = forms.SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            return TasksListView.as_view()(request)


class TaskDetailView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "track/tasks/task_detail.html"
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "track/tasks/task_add.html"
    fields = (
        "title", "due_date", "status", "date_completed",
        "start_time", "end_time", "effort_hours", "objective", "sprint",
        "backlog",
    )    
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(TaskCreateView, self).form_valid(form)
    

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "track/tasks/task_edit.html"
    fields = (
        "title", "due_date", "status", "date_completed",
        "start_time", "end_time", "effort_hours", "objective", "sprint",
        "backlog",
    )
    success_url = reverse_lazy("tasks_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(TaskUpdateView, self).form_valid(form)
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "track/tasks/task_delete.html"
    success_url = reverse_lazy("tasks_list")

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return redirect(reverse_lazy("unauthorized"))
        return super().post(self.request, *args, **kwargs)
    

#========================= for sprints
    
class SprintListView(LoginRequiredMixin, ListView):
    model = Sprint
    template_name = "track/sprints/sprints.html"
    context_object_name = "sprints"

    def get_queryset(self):
        return Sprint.objects.filter(owner=self.request.user).order_by("-end_date")   


class SprintCreateView(LoginRequiredMixin, CreateView):
    model = Sprint
    template_name = "track/sprints/sprint_add.html"
    fields = (
        "title", "description", "start_date", "end_date", "status",
        "comments",
    )    
    success_url = reverse_lazy("sprints_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(SprintCreateView, self).form_valid(form)
    

class SprintDetailView(LoginRequiredMixin, DetailView):
    model = Sprint
    template_name = "track/sprints/sprint_detail.html"
    context_object_name = "sprint"

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return redirect(reverse_lazy("unauthorized"))
        return super().get(self.request, *args, **kwargs)


class SprintUpdateView(LoginRequiredMixin, UpdateView):
    model = Sprint
    template_name = "track/sprints/sprint_edit.html"
    fields = (
        "title", "description", "start_date", "end_date", "status",
        "comments",
    )
    success_url = reverse_lazy("sprints_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(SprintUpdateView, self).form_valid(form)
    

class SprintDeleteView(LoginRequiredMixin, DeleteView):
    model = Sprint
    template_name = "track/sprints/sprint_delete.html"
    success_url = reverse_lazy("sprints_list")

    def get(self, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return redirect(reverse_lazy("unauthorized"))
        return super().post(self.request, *args, **kwargs)


class BacklogList(ListView):
    model = models.Task
    template_name = "track/tasks/backlog.html"
    context_object_name = "backlog"

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user, backlog=True)