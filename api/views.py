from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from track.models import (
    Task, Goal, Objective, Sprint
)
from api.serializers import (
    TaskSerializer, GoalSerializer, ObjectiveSerializer, 
    SprintSerializer
)

# Goals

class GoalListAPIView(ListCreateAPIView):
    serializer_class = GoalSerializer
    
    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)


class GoalDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(owner=self.request.user)


class TaskListAPIView(ListAPIView):
    serializer_class = TaskSerializer
    # queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    

class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class ObjectiveListAPIView(ListAPIView):
    serializer_class = ObjectiveSerializer
    queryset = Objective.objects.all()

    def get_queryset(self):
        return Objective.objects.filter(owner=self.request.user)


class SprintListAPIView(ListAPIView):
    serializer_class = SprintSerializer
    queryset = Sprint.objects.all()

    def get_queryset(self):
        return Sprint.objects.filter(owner=self.request.user)