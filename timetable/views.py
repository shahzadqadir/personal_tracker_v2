from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from timetable.models import TimeTable, TimeTableTask
from timetable.forms import TimeTableForm, TimeTableTaskForm


class TimeTableListView(generic.ListView, LoginRequiredMixin):
    model = TimeTable
    context_object_name = 'timetables'
    template_name = 'timetable/timetable_list.html'
    

    def get_queryset(self):
        return TimeTable.objects.filter(owner=self.request.user)
    
class TimeTableCreateView(generic.CreateView, LoginRequiredMixin):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'timetable/timetable_add.html'
    success_url = reverse_lazy("sprints_list")