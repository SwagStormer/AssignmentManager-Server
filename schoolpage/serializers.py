from schoolpage.models import Announcement
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

    def create(self, validated_data):
        raise ValidationError("You cannot create announcements")
