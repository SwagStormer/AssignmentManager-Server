from django.contrib import admin

# Register your models here.
from .models import Task, MyUser, Course, Version
# Register your models here.


admin.site.register(MyUser)


admin.site.register(Task)

admin.site.register(Course)

admin.site.register(Version)
