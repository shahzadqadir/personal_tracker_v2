from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
# default_user = User.objects.get(id=1)


class Goal(models.Model):
    description = models.CharField(max_length=255)
    status = models.CharField(max_length=100, default="notdone")
    target_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_goals", null=True, blank=True
    )

    def __str__(self):
        if len(self.description) > 50:
            return self.description[:50] + " ..."
        return self.description

    def short_description(self):
        return self.description[:50] + " ..."

    def get_objectives_count(self):
        return self.goal_objectives.count()


class Objective(models.Model):
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=100, blank=True, null=True)
    due_date = models.DateField(default=timezone.now)
    completion_date = models.DateField(blank=True, null=True)
    effort_hours = models.FloatField(default=2.0)
    effort_hours_left = models.FloatField(default=2.0)
    status = models.CharField(max_length=100, default="notdone")
    progress = models.PositiveIntegerField(default=0)
    goal = models.ForeignKey(
        Goal,
        on_delete=models.CASCADE,
        related_name="goal_objectives",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_objectives",
        null=True,
        blank=True,
    )

    def __str__(self):
        if len(self.description) > 50:
            return self.description[:50] + " ..."
        return self.description

    @property
    def short_description(self):
        return self.description[:50]

    @property
    def get_hours_worked(self):
        sum = 0
        for task in self.objective_tasks.all():
            sum += task.end_time.hour - task.start_time.hour
        return sum

    @property
    def get_tasks_count(self):
        return self.objective_tasks.count()

    @property
    def get_completed_tasks_count(self):
        return self.objective_tasks.filter(status="complete").count()


class Sprint(models.Model):
    STATUS_CHOICES = {
        "notstarted": "notstarted",
        "inprogress": "inprogress",
        "complete": "complete",
    }
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=100, default="notstarted", choices=STATUS_CHOICES
    )
    comments = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_sprints",
        null=True,
        blank=True,
    )

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + " ..."
        return self.title

    @property
    def short_title(self):
        return self.title[:50]

    @property
    def get_time_spent_this_sprint(self):
        sum = 0
        for task in self.sprint_tasks.all():
            sum += task.end_time.hour - task.start_time.hour
        return sum

    @property
    def get_time_planned_this_sprint(self):
        sum = 0
        for task in self.sprint_tasks.all():
            sum += task.effort_hours
        return sum

    @property
    def get_hours_worked_per_day(self):
        hours_per_date = {}
        for task in self.sprint_tasks.order_by("-due_date"):
            if task.status == "complete":
                if str(task.due_date.date()) not in hours_per_date:
                    hours_per_date[str(task.due_date.date())] = (
                        task.end_time.hour - task.start_time.hour
                    )
                else:
                    hours_per_date[str(task.due_date.date())] += (
                        task.end_time.hour - task.start_time.hour
                    )
        return hours_per_date

    @property
    def get_percentage_completed(self):
        all_tasks = self.sprint_tasks.count()
        if all_tasks == 0:
            return 0
        completed_tasks = self.sprint_tasks.filter(status="complete").count()
        return round((completed_tasks / all_tasks) * 100, 2)

    @property
    def get_percentage_completed_by_date(self):

        tasks_by_date = {}
        for task in self.sprint_tasks.order_by("-due_date"):
            if str(task.due_date.date()) not in tasks_by_date:
                tasks_by_date[str(task.due_date.date())] = 1
            else:
                tasks_by_date[str(task.due_date.date())] += 1

        completed_tasks_by_date = {}
        for task in self.sprint_tasks.order_by("-due_date"):
            if task.status == "complete":
                if str(task.due_date.date()) not in completed_tasks_by_date:
                    completed_tasks_by_date[str(task.due_date.date())] = 1
                else:
                    completed_tasks_by_date[str(task.due_date.date())] += 1

        tasks_percentage = {}
        for dat in tasks_by_date:
            try:
                tasks_percentage[dat[5:]] = (
                    completed_tasks_by_date[dat] / tasks_by_date[dat]
                ) * 100
            except KeyError:
                pass

        return tasks_percentage


class Task(models.Model):
    STATUS_CHOICES = {
        "notdone": "notdone",
        "inprogress": "inprogress",
        "complete": "complete",
    }
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, default="notdone", choices=STATUS_CHOICES)
    date_completed = models.DateTimeField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    effort_hours = models.PositiveIntegerField(default=2, blank=True, null=True)
    objective = models.ForeignKey(
        Objective,
        on_delete=models.CASCADE,
        related_name="objective_tasks",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_tasks", null=True, blank=True
    )
    sprint = models.ForeignKey(
        Sprint,
        on_delete=models.CASCADE,
        related_name="sprint_tasks",
        null=True,
        blank=True,
    )
    backlog = models.BooleanField(default=False, null=True, blank=True)
    date_added = models.DateField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        if len(self.title) > 50:
            return self.title[:50] + " ..."
        return self.title

    @property
    def short_title(self):
        return self.title[:50]

    @property
    def get_hours_worked(self):
        return self.end_time.hour - self.start_time.hour
