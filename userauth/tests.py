from django.test import TestCase

from .models import CustomUser

class TestCustomUser(TestCase):

    def test_create_user(self):
        user = CustomUser.objects.create(
            username="test123",
            password="cisco123",
            email="test123@gmail.com"
        )
        self.assertEqual(user.username, "test123")
        self.assertEqual(user.email, "test123@gmail.com")

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            username="test111",
            email="test111@gmail.com",
            password="cisco123"
        )
        self.assertEqual(user.username, "test111")
        self.assertEqual(user.email, "test111@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)