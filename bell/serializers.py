from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Schedule, Period, Date


class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request.user.is_authenticated and request.user.is_superuser:
            d = Date(**validated_data)
            d.save()
            return d
        else:
            raise ValidationError("Only admins can make these")


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request.user.is_authenticated and request.user.is_superuser:
            d = Date(**validated_data)
            d.save()
            return d
        else:
            raise ValidationError("Only admins can make these")


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

    def create(self, validated_data):
        if self.request.user.is_validated and self.request.user.is_superuser:
            d = Date(**validated_data)
            d.save()
            return d
        else:
            return ValidationError("Only admins can make these")
