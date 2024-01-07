from django.test import TestCase
from django.contrib.auth import get_user_model

from track.models import (
    Goal, Objective, Task, Sprint
)

class TestTrackModels(TestCase):


    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create(
            username="test1",
            password="password1",
            email="test1@email.com"
        )
        self.goal = None
        

    def test_create_goal_default_date(self):
        self.goal = Goal.objects.create(
            description="test goal 1",
            status="test status 1",
            owner=self.owner
        )
        self.assertEqual(len(Goal.objects.all()), 1)
        self.assertEqual(self.goal.status, "test status 1")
        self.assertEqual(self.goal.owner, self.owner)

    def test_create_objective_with_defaults(self):
        goal = Goal.objects.create(
            description="test goal",
            status="test status",
            owner=self.owner
        )
        self.objective = Objective.objects.create(
            description="objective 1 for goal 1",
            goal = goal,
            owner=self.owner
        )
        self.assertEqual(len(Objective.objects.all()), 1)
        self.assertEqual(self.objective.description, "objective 1 for goal 1")


    def test_create_task_with_defaults(self):
        goal = Goal.objects.create(
            description="test goal",
            status="test status",
            owner=self.owner
        )
        objective = Objective.objects.create(
            description="objective 1 for goal 1",
            goal = goal,
            owner=self.owner
        )
        task = Task.objects.create(
            title="test task 1",
            objective = objective,
            owner = self.owner
        )
        self.assertEqual(len(Task.objects.all()), 1)
        self.assertEqual(task.title, "test task 1")
        self.assertEqual(task.owner, self.owner)

    def test_create_sprint_with_defaults(self):
        goal = Goal.objects.create(
            description="test goal",
            status="test status",
            owner=self.owner
        )
        objective = Objective.objects.create(
            description="objective 1 for goal 1",
            goal = goal,
            owner=self.owner
        )
        task = Task.objects.create(
            title="test task 1",
            objective = objective,
            owner = self.owner
        )
        sprint = Sprint.objects.create(
            title="test sprint",
            owner=self.owner
        )
        self.assertEqual(len(Sprint.objects.all()), 1)
        self.assertEqual(sprint.title, "test sprint")
    
