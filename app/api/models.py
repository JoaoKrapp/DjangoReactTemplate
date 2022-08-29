from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    code = models.CharField(max_length=10, default="", unique=True)
    name = models.CharField(max_length=255, default="")

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()