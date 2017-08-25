from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class MyUser(AbstractUser):
    sis_username = models.CharField(max_length=20)
    sis_password = models.CharField(max_length=40)


class Course(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=10)
    user = models.ForeignKey(MyUser)

    def __str__(self):
        return '%s' % self.name


class Task(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateField()
    is_finished = models.BooleanField(default=False)
    snooze_until = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(Course)

    def __str__(self):
        return '%s' % self.name


class Version(models.Model):
    number = models.IntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.number



