from django.contrib import admin
from schoolpage.models import Announcement
# Register your models here.


class AnnouncementAdmin(admin.ModelAdmin):
    pass

admin.site.register(Announcement, AnnouncementAdmin)
