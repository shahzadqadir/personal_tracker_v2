from django import forms

from timetable.models import TimeTable, TimeTableTask

class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ('description', 'valid_from', 'valid_until', 'comments')


class TimeTableTaskForm(forms.ModelForm):
    class Meta:
        model = TimeTableTask
        fields = ('start_time', 'end_time', 'description', 'timetable', 'comments')


