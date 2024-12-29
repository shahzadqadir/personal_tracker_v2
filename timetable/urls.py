from django.urls import path

from timetable.views import TimeTableListView, TimeTableCreateView

urlpatterns = [
    path('timetable_list/', TimeTableListView.as_view(), name='timetable_list'),
    path('timetable_add/', TimeTableCreateView.as_view(), name='timetable_add'),
]