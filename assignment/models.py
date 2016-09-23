from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MyUser(AbstractUser):
    pass


class Docket(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(MyUser)


class Task(models.Model):
    name = models.CharField(max_length=30)
    time_estimate = models.IntegerField()
    importance = models.IntegerField(null=True, blank=True)
    done_today = models.BooleanField(default=False)
    due_date = models.DateField()
    daily_time_amount = models.IntegerField(null=True, blank=True)
    docket = models.ForeignKey(Docket)




