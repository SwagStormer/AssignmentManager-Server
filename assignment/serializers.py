from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from django.utils import timezone
from rest_framework.decorators import list_route, api_view
from .scraper import is_valid
from .models import MyUser, Course, Task, Version
from .importance import importance_calc


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        time_estimate = validated_data["time_estimate"]
        due_date = validated_data["due_date"]
        i = importance_calc(due_date, time_estimate)
        print(timezone.now())
        task = Task(
            importance=i[0],
            daily_time_amount=i[1],
            name=validated_data["name"],
            time_estimate=time_estimate,
            due_date=due_date,
            Course=validated_data["Course"],
            done_today=False
        )
        task.save()
        return task


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        if is_valid(validated_data['sis_username'], validated_data['sis_password']):
            user = MyUser(
                email=validated_data['email'],
                username=validated_data['username'],
                sis_username=validated_data['sis_username'],
                sis_password=validated_data['sis_password']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        else:
            raise ValidationError("Must have all fields")


class MyUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = ('password',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        raise MethodNotAllowed()


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if not request.user.is_staff:
            raise ValidationError("Only Admins can do this")
