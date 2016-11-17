from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Schedule, Span


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule


class SpanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Span
