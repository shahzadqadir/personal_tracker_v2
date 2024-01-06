from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
default_user = User.objects.get(id=1)

class Goal(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=100, default="notdone")
    target_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name="user_goals")

    def __str__(self):
        if len(self.description) > 50:
            return self.description[:50] + "..."
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
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, 
                             related_name="goal_objectives")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name="user_objectives")

    def __str__(self):
        if len(self.description) > 50:
            return self.description[:50] + " ..."
        return self.description
    
    @property
    def short_description(self):
        return self.description[:50]


class Task(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=100, default="notdone")
    date_completed = models.DateTimeField(null=True, blank=True)
    start_time = models.TimeField(timezone.now)
    end_time = models.TimeField(blank=True, null=True)
    objective = models.ForeignKey(Objective, on_delete=models.CASCADE, 
                                  related_name="objective_tasks")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
                              related_name="user_tasks")
    
    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + " ..."
        return self.title
    
    @property
    def short_title(self):
        return self.title[:50]
