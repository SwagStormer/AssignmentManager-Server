from rest_framework import viewsets
from datetime import datetime
from .serializers import ScheduleSerializer, PeriodSerializer, DateSerializer
from .models import Schedule, Period, Date
# Create your views here.


class DateViewSet(viewsets.ModelViewSet):
    serializer_class = DateSerializer
    queryset = Date.objects.all()


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        q = self.request.query_params.get

        if q('today'):
            return Schedule.objects.filter(date=datetime.now().strftime("%A").upper())
        else:
            return Schedule.objects.all()


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()

    def get_queryset(self):

        q = self.request.query_params.get

        if q('now'):
            date = Date.objects.filter(date=datetime.now().strftime("%A").upper())
            schedule = Schedule.objects.filter(date=date)[0]
            periods = Period.objects.filter(schedule=schedule)
            now = datetime.now().time()
            return [period for period in periods if period.start_time <= now <= period.end_time]
        else:
            return Period.objects.all()
