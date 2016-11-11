from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Schedule, Period


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
