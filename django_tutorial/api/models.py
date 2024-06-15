from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class CustomUser(AbstractUser):
    """Creating customized user model"""

    username = models.CharField(max_length=100)
    role = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
