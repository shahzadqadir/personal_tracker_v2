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
    success_url = reverse_lazy("timetable_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(TimeTableCreateView, self).form_valid(form)
    

