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
