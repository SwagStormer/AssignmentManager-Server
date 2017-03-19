from django.db import models

# Create your models here.


class Announcement(models.Model):
    header = models.TextField()
    content = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.header

