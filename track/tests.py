from django.test import TestCase
from django.contrib.auth import get_user_model

from track.models import Goal, Objective

class TestTrackModels(TestCase):

    def setUp(self):
        User = get_user_model()
        self.owner = User.objects.create(
            username="test1",
            password="password1",
            email="test1@email.com"
        )

    def test_create_goal_default_date(self):
        goal = Goal.objects.create(
            description="test goal 1",
            status="test status 1",
            owner=self.owner
        )
        self.assertEqual(len(Goal.objects.all()), 1)
        self.assertEqual(goal.status, "test status 1")
        self.assertEqual(goal.owner, self.owner)

    def test_create_goal_with_date(self):
        goal = Goal.objects.create(
            description="test goal 2",
            status="test status 2",
            target_date="2024-06-01",
            owner=self.owner
        )
        self.assertEqual(goal.status, "test status 2")

    def test_create_objective_with_defaults(self):
        goal = Goal.objects.create(
            description="test goal",
            status="test status",
            owner=self.owner
        )
        objective = Objective.objects.create(
            description="objective 1 for goal 1",
            goal = goal
        )
        self.assertEqual(len(Objective.objects.all()), 1)
        self.assertEqual(objective.description, "objective 1 for goal 1")
