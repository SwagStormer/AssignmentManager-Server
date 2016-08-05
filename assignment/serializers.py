from rest_framework import serializers
from models import MyUser, Schedule, Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        exclude = ('importance', 'daily_time_amount', 'schedule', )

    def create(self, validated_data):
        request = self.context.get('request')
        s = Schedule.objects.filter(user=request.user)
        s.filter(name=validated_data["schedule"])
        assignment = Assignment(
            name=validated_data["name"],
            time_estimate=validated_data["time_estimate"],
            due_date=validated_data["due_date"],
            schedule=s
        )
        assignment.save()
        return assignment


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MyUserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        exclude = ('password',)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        exclude = ('user', )

    def create(self, validated_data):
        request = self.context.get('request')
        print(request.user.id)
        schedule = Schedule(
            name=validated_data["name"],
            user=request.user
        )
        schedule.save()
        return schedule
