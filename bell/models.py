from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Date(models.Model):
    DAYS = (
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),

    )
    date = models.CharField(choices=DAYS, max_length=9)

    def __str__(self):
        return '%s' % self.date


class Schedule(models.Model):
    name = models.CharField(max_length=20)
    schedule_active = models.DateField(null=True, blank=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.ManyToManyField(Date)

    def __str__(self):
        return '%s' % self.name


class Period(models.Model):
    schedule = models.ForeignKey(Schedule)
    name = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return '%s' % self.name
