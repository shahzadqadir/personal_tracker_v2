from track.models import Task, Objective, Goal, Sprint

from rest_framework import serializers
from track import models


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            "id": {"read_only": True}
        }
        fields = ("id", "description", "status", "target_date")
        model = Goal

    def create(self, validated_data):
        request = self.context.get("request")
        goal = models.Goal.objects.create(
            description=validated_data["description"],
            status=validated_data["status"],
            target_date=validated_data["target_date"],
            owner=request.user
        )
        return goal


class ObjectiveSerializer(serializers.ModelSerializer):
    goal = GoalSerializer()
    class Meta:
        extra_kwargs = {
            "id": {"read_only": True}
        }
        model = Objective
        fields = ("id", "description", "category", "due_date",
                  "completion_date", "effort_hours", "effort_hours_left",
                  "status", "progress", "goal",
        )

class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "id": {"read_only": True}
        }
        model = Sprint
        fields = ("id", "title", "description", "start_date", "end_date", "status", 
                "comments", "owner")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "id": {"read_only": True}
        }
        model = Task
        fields = ("id", "title", "due_date", "status", "date_completed", 
                "start_time", "end_time", "effort_hours", "objective",
                "owner", "sprint")



