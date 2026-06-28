from rest_framework import serializers
from .models import Habit
from .validators import validate

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ("id", "user")

    def validate(self, attrs):
        return validate(self, attrs)
