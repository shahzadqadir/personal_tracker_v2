from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# default_user = User.objects.get(id=1)


class TimeTable(models.Model):
    description = models.CharField(blank=True, null=True)
    valid_from = models.DateField(default=timezone.now)
    valid_until = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.description


class TimeTableTask(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.CharField(max_length=1000)
    timetable = models.ForeignKey(TimeTable, on_delete=models.CASCADE, related_name='timetable_tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    comments = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.description
    
