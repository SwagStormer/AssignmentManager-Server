from rest_framework import viewsets
from .serializers import ScheduleSerializer, PeriodSerializer
from .models import Schedule, Period
# Create your views here.


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)


class PeriodViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodSerializer
    queryset = Period.objects.all()
