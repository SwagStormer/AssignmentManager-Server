from django.contrib import admin

# Register your models here.
from .models import Assignment, MyUser, Schedule
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyUser, UserAdmin)


class AssignmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Assignment,AssignmentAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    pass
admin.site.register(Schedule, ScheduleAdmin)
