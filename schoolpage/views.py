from rest_framework import viewsets
from schoolpage.models import Announcement
from schoolpage.serializers import AnnouncementSerializer
# Create your views here.


class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all()


