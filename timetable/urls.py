from django.urls import path

from timetable.views import (
    TimeTableListView, 
    TimeTableCreateView,
    TimeTableRelatedTasksView,
    TimeTableTaskListView,
    TimeTableTaskCreateView,
    TimeTableTaskDetailView,
    TimeTableTaskDeleteView,
    TimeTableTaskUpdateView
    
)

urlpatterns = [
    path('timetable_list/', TimeTableListView.as_view(), name='timetable_list'),
    path('timetable_add/', TimeTableCreateView.as_view(), name='timetable_add'),
    path('<int:pk>/related_tasks/', TimeTableRelatedTasksView.as_view(), name='timetable_relatedtasks'),
    path('timetabletask_list/', TimeTableTaskListView.as_view(), name='timetabletask_list'),
    path('timetabletask_add/', TimeTableTaskCreateView.as_view(), name='timetabletask_add'),
    path('timetabletask/<int:pk>/detail/', TimeTableTaskDetailView.as_view(), name='timetabletask_detail'),
    path('timetabletask/<int:pk>/update/', TimeTableTaskUpdateView.as_view(), name='timetabletask_update'),
    path('timetabletask/<int:pk>/delete/', TimeTableTaskDeleteView.as_view(), name='timetabletask_delete'),
]