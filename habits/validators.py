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
            "A beneficial habit cannot have both a reward and a connected pleasant habit."
        )

    if not is_pleasant and duration > timedelta(seconds=120):
        raise serializers.ValidationError("The execution time must not exceed 120 seconds.")

    if not is_pleasant and connected_habit and not connected_habit.is_pleasant:
        raise serializers.ValidationError(
            "Only habits marked as pleasant can be used as connected habits."
        )

    if is_pleasant and (reward or connected_habit):
        raise serializers.ValidationError(
            "A pleasant habit cannot have a reward or a connected habit."
        )

    if period and period >= 7:
        raise serializers.ValidationError(
            "A habit cannot be performed less frequently than once every 7 days."
        )

    return attrs
