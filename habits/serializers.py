from django.utils import timezone

from rest_framework import serializers

from .models import Habit
from .validators import validate


def current_time():
    return timezone.localtime().time()


class HabitSerializer(serializers.ModelSerializer):
    time = serializers.TimeField(format="%H:%M", default=current_time)

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("id", "user")

    def validate(self, attrs):
        return validate(self, attrs)
