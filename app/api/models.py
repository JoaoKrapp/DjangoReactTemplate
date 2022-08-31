from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def upload_to(instance, filename):
    return f'avatar/{filename}'

class Person(models.Model):
    code = models.CharField(max_length=10, default="", unique=True)
    name = models.CharField(max_length=255, default="")

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatar/')
    