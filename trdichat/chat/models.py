from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)


class EmailUs(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return self.Name + ' ' + self.Email


class CustomUser(models.Model):
    GENDESER_CHOICES = (
        ('M', 'Mr.'),
        ('F', 'Miss.'),
    )

    gender = models.CharField(max_length=1, choices=GENDESER_CHOICES, blank=True)

    def __str__(self):
        return self.gender