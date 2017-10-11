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
        queryset = Schedule.objects.all()
        if q('today'):
            abnormal = queryset.filter(
                schedule_active__isnull=False,
                schedule_active=datetime.now())
            if abnormal.count() == 1:
                queryset = abnormal
            else:
                queryset = queryset.filter(date__date=datetime.now().strftime("%A").upper())
        return queryset


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
    permission_classes = [IsAdminOrReadOnly, ]

    def get_queryset(self):
        q = self.request.query_params.get
        queryset = Period.objects.all()

        date = Date.objects.filter(date=datetime.now().strftime("%A").upper())
        schedules = Schedule.objects.filter(
            schedule_active__isnull=False,
            schedule_active=datetime.now())
        if schedules.count() == 1:
            schedule = schedules.first()
        else:
            schedule = Schedule.objects.filter(schedule_active__isnull=True, date=date).first()

        if q('now'):
            queryset = queryset.filter(
                schedule=schedule, start_time__lte=datetime.now(), end_time__gte=datetime.now())
        elif q('today'):
            queryset = queryset.filter(schedule=schedule)
        return queryset
