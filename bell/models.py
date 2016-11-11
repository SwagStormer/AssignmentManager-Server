from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Schedule(models.Model):
    name = models.CharField(max_length=20)
    start_time = models.TimeField()


class Period(models.Model):
    schedule = models.ForeignKey(Schedule)
    name = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
