from rest_framework import viewsets
from .serializers import ScheduleSerializer, SpanSerializer
from .models import Schedule, Span
# Create your views here.


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user)


class SpanViewSet(viewsets.ModelViewSet):
    serializer_class = SpanSerializer
    queryset = Span.objects.all()
