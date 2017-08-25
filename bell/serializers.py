from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Schedule, Period, Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'
