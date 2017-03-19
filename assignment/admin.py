from django.contrib import admin

# Register your models here.
from .models import Task, MyUser, Course, Version
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyUser, UserAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)


class VersionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Version, VersionAdmin)
