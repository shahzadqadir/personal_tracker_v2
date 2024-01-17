from track.models import Task, Objective, Goal, Sprint

from rest_framework import serializers


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        exclude = ("id", "owner", )

class ObjectiveSerializer(serializers.ModelSerializer):
    goal = GoalSerializer()
    class Meta:
        model = Objective
        fields = ("description", "category", "due_date",
                  "completion_date", "effort_hours", "effort_hours_left",
                  "status", "progress", "goal",
        )

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

