from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Goal(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    target_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Objective(models.Model):
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(default=timezone.now)
    completion_date = models.DateField(blank=True, null=True)
    effort_hours = models.FloatField(default=2.0)
    effort_hours_left = models.FloatField(default=2.0)
    status = models.CharField(max_length=100,default="notdone")
    progress = models.PositiveIntegerField(default=0)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="goal_objectives")

    def __str__(self):
        return self.description[:50]

