from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Service(models.Model):
    title = models.CharField(max_length=150)
    detail = models.TextField()

class DemoSession(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    preferred_day = models.CharField(max_length=20)
    preferred_time = models.TimeField()

class LoginRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=timezone.now)


