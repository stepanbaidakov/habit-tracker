from datetime import timedelta

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Habit

# Create your tests here.


class HabitsTestCase(APITestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="test", email="test@email.com", password="123qwe")
        self.pleasant_habit = Habit.objects.create(
            title="test",
            action="test",
            is_pleasant=True,
            duration=timedelta(minutes=1),
            is_public=True,
            user=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        self.data = {
            "title": "test",
            "action": "test",
            "is_pleasant": False,
            "duration": "00:01:00",
            "connected_habit": self.pleasant_habit.id,
            "is_public": True,
            "time": "09:00",
            "last_sent": "2026-07-18T20:47:00",
        }
        response = self.client.post("/habit/", data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.json(),
            {
                "id": 2,
                "time": "09:00",
                "title": "test",
                "location": None,
                "action": "test",
                "is_pleasant": False,
                "period": 1,
                "reward": None,
                "duration": "00:01:00",
                "is_public": True,
                "last_sent": "2026-07-18T20:47:00+02:00",
                "user": self.user.id,
                "connected_habit": self.pleasant_habit.id,
            },
        )
