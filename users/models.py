from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    chat_id = models.BigIntegerField(null=True, blank=True)
    telegram_username = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.email}"
