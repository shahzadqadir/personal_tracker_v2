from django import forms
from django.utils import timezone

from track.models import Task, Objective, Goal

class GoalsForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ("description", "status", "target_date")


class ObjectivesForm(forms.ModelForm):
    class Meta:
        model = Objective
        exclude = ("owner",)
        # fields = ("description", "category", "due_date", "completion_date",
        #           "effort_hours", "effort_hours_left", "status", "progress", "goal",
        #           )
    