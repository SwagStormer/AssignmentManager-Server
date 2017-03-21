from django.contrib import admin
from bell.models import Schedule, Period, Date
# Register your models here.


class ScheduleAdmin(admin.ModelAdmin):
    pass

admin.register(Schedule, ScheduleAdmin)


class PeriodAdmin(admin.ModelAdmin):
    pass

admin.register(Period, PeriodAdmin)


class DateAdmin(admin.ModelAdmin):
    pass

admin.register(Date, DateAdmin)