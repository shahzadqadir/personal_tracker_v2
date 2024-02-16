from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from track import models
from api import serializers


class EndPointsList(TemplateView):
    template_name = "api/endpoints_list.html"


class GoalListAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.GoalSerializer
    
    def get_queryset(self):
        return models.Goal.objects.filter(owner=self.request.user)


class GoalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GoalSerializer

    def get_queryset(self):
        return models.Goal.objects.filter(owner=self.request.user)


class GoalObjectivesList(generics.ListAPIView):
    serializer_class = serializers.ObjectiveSerializer

    def get_queryset(self):
        objectives = (
            models.Objective.objects.filter(goal_id=self.kwargs.get("goal_pk")))
        return objectives


class TaskListAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer
    # queryset = Task.objects.all()

    def get_queryset(self):
        return models.Task.objects.filter(owner=self.request.user)
    

class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.filter(owner=self.request.user)


class ObjectiveListAPIView(generics.ListAPIView):
    serializer_class = serializers.ObjectiveSerializer
    queryset = models.Objective.objects.all()

    def get_queryset(self):
        return models.Objective.objects.filter(owner=self.request.user)


class ObjectiveDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ObjectiveSerializer
    queryset = models.Objective.objects.all()


class ObjectiveTasksAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.filter(objective_id=self.kwargs.get("objective_pk"))


class SprintListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = serializers.SprintSerializer
    # queryset = get_object_or_404(models.Sprint, pk=self.kwargs.get("pk"))

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Sprint.objects.filter(owner=self.request.user)
        return None

class SprintTasksListAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskSerializer

    def get_queryset(self):
        return models.Task.objects.filter(sprint_id=self.kwargs.get("sprint_pk"))


class SprintDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Sprint.objects.all()
    serializer_class = serializers.SprintSerializer