from rest_framework import viewsets
from .serializers import ScheduleSerializer, PeriodSerializer
from .models import Schedule, Period
# Create your views here.


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
