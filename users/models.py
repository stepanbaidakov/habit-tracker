from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    telegram_username = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} - {self.email}"
