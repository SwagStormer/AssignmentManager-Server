from django.contrib import admin
from bell.models import Schedule, Period, Date
# Register your models here.


class ScheduleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Schedule, ScheduleAdmin)


class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Period, PeriodAdmin)


class DateAdmin(admin.ModelAdmin):
    pass

admin.site.register(Date, DateAdmin)