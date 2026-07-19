from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "telegram_username"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        User = get_user_model()
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.get("password")
        if password:
            password = validated_data.pop("password")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)

        instance.save()
        return instance
