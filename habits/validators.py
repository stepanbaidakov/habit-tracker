from datetime import timedelta
from rest_framework import serializers

def validate(self, attrs):
    is_pleasant = attrs.get("is_pleasant", self.instance.is_pleasant if self.instance else None)
    reward = attrs.get("reward", self.instance.reward if self.instance else None)
    connected_habit = attrs.get("connected_habit", self.instance.connected_habit if self.instance else None)
    duration = attrs.get("duration", self.instance.duration if self.instance else None)
    period = attrs.get("period", self.instance.period if self.instance else None)

    if reward and connected_habit and not is_pleasant:
        raise serializers.ValidationError(
            "Полезная привычка не должна иметь одновременно награду и связанную приятную привычку.")

    if not is_pleasant and duration > timedelta(seconds=120):
        raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")

    if not is_pleasant and connected_habit and not connected_habit.is_pleasant:
        raise serializers.ValidationError(
            "В связанные привычки могут попадать только привычки с признаком приятной привычки.")

    if is_pleasant and (reward or connected_habit):
        raise serializers.ValidationError(
            "У приятной привычки не может быть вознаграждения или связанной привычки.")

    if period >= 7:
        raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")
