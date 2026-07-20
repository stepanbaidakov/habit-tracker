from django.db import models
from django.utils import timezone

from config.settings import AUTH_USER_MODEL

# Create your models here.


def current_time():
    return timezone.localtime().time()


class Habit(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits")
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50, blank=True, null=True)
    time = models.TimeField(default=current_time)
    action = models.TextField()
    is_pleasant = models.BooleanField()
    connected_habit = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="habits"
    )
    period = models.IntegerField(default=1, null=True, blank=True)
    reward = models.CharField(max_length=50, null=True, blank=True)
    duration = models.DurationField()
    is_public = models.BooleanField()
    last_sent = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Habits"
        verbose_name = "Habit"
