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
            s = Schedule(**validated_data)
            s.save()
            return s
        else:
            raise ValidationError("Only admins can make these")


class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request.user.is_authenticated and request.user.is_superuser:
            p = Period(**validated_data)
            p.save()
            return p
        else:
            raise ValidationError("Only admins can make these")
