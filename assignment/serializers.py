from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from .scraper import is_valid
from .management.commands.update_grades import update_or_create_grades
from .models import MyUser, Course, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('snooze_until', 'is_finished')


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        if is_valid(validated_data['sis_username'], validated_data['sis_password']):
            user = MyUser(
                username=validated_data['username'],
                sis_username=validated_data['sis_username'],
                sis_password=validated_data['sis_password']
            )
            user.set_password(validated_data['password'])
            user.save()
            update_or_create_grades(user)
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

