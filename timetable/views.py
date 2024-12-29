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
    

class TimeTableRelatedTasksView(LoginRequiredMixin, generic.ListView):
    model = TimeTable
    template_name = 'timetable/timetable_relatedtasks.html'
    context_object_name = 'timetable'

    def get_queryset(self):
        return TimeTable.objects.filter(owner=self.request.user)[0]
    

class TimeTableTaskListView(LoginRequiredMixin, generic.ListView):
    model = TimeTableTask
    template_name = 'timetable/timetabletask_list.html'
    context_object_name = 'timetabletasks'

    def get_queryset(self):
        return TimeTableTask.objects.filter(owner=self.request.user)

class TimeTableTaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = TimeTableTask
    form_class = TimeTableTaskForm
    template_name = 'timetable/timetabletask_add.html'
    success_url = reverse_lazy('timetable_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.save()
        return super(TimeTableTaskCreateView, self).form_valid(form)
    

class TimeTableTaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = TimeTableTask
    template_name = 'timetable/timetabletask_detail.html'
    context_object_name = 'timetabletask'


class TimeTableTaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TimeTableTask
    template_name = 'timetable/timetabletask_delete.html'
    success_url = reverse_lazy('timetable_list')


class TimeTableTaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TimeTableTask
    template_name = 'timetable/timetabletask_update.html'
    form_class = TimeTableTaskForm
    
    def get_success_url(self):
        return reverse("timetabletask_detail", kwargs={"pk": self.object.id})