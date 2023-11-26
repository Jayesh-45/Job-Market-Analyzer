from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password=models.CharField(max_length=30, unique=True)
