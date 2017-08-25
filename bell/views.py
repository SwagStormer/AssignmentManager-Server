from rest_framework import viewsets
from datetime import datetime

from bell.permissions import IsAdminOrReadOnly
from .serializers import ScheduleSerializer, PeriodSerializer, DateSerializer
from .models import Schedule, Period, Date
# Create your views here.


class DateViewSet(viewsets.ModelViewSet):
    serializer_class = DateSerializer
    queryset = Date.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]

    def get_queryset(self):
        q = self.request.query_params.get

        if q('today'):
            return Schedule.objects.filter(date=datetime.now().strftime("%A").upper())
        else:
            return Schedule.objects.all()


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]

    def get_queryset(self):
        q = self.request.query_params.get
        if q('now'):
            date = Date.objects.filter(date=datetime.now().strftime("%A").upper())
            schedule = Schedule.objects.filter(date=date)
            now = datetime.now().time()
            periods = Period.objects.filter(
                schedule=schedule, start_time__lte=now, end_time__gte=now)
            return periods
        elif q('today'):
            date = Date.objects.filter(date=datetime.now().strftime("%A").upper())
            schedule = Schedule.objects.filter(date=date)
            return Period.objects.filter(schedule=schedule)
        else:
            return Period.objects.all()
