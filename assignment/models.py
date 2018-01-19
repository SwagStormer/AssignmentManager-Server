from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models import CASCADE


class MyUser(AbstractUser):
    pass


class Course(models.Model):
    name = models.CharField(max_length=30)
    grade = models.CharField(max_length=10)
    user = models.ForeignKey(MyUser, on_delete=CASCADE)

    def __str__(self):
        return '%s' % self.name


class Task(models.Model):
    name = models.CharField(max_length=30)
    due_date = models.DateField()
    is_finished = models.BooleanField(default=False)
    snooze_until = models.DateTimeField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=CASCADE)

    def __str__(self):
        return '%s' % self.name
