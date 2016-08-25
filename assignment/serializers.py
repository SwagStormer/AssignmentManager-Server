from rest_framework import serializers
from models import MyUser, Schedule, Assignment
from importance import importance_calc


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        exclude = ('importance', 'daily_time_amount', 'done_today',)

    def create(self, validated_data):
        time_estimate = validated_data["time_estimate"]
        due_date = validated_data["due_date"]
        i = importance_calc(due_date, time_estimate)
        assignment = Assignment(
            importance=i[0],
            daily_time_amount=i[1],
            name=validated_data["name"],
            time_estimate=time_estimate,
            due_date=due_date,
            schedule=validated_data["schedule"],
            done_today=False
        )
        assignment.save()
        return assignment


class AssignmentReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment


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
