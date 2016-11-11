from django.contrib import admin

# Register your models here.
from .models import Task, MyUser, Docket, Version
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(MyUser, UserAdmin)


class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Task, TaskAdmin)


class DocketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Docket, DocketAdmin)


class VersionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Version, VersionAdmin)
