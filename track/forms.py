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
        
        
class SearchForm(forms.Form):
    search = forms.CharField(label="", required=False,
                             widget=forms.TextInput(attrs={"placeholder": "Search ..."}))
    
    def __str__(self):
        return "Search..."

    