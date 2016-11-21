from pprint import pprint

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils import timezone

from .models import MyUser, Docket, Task, Version
from .importance import importance_calc
from .scraper.scraper import request_grades


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task

    def create(self, validated_data):
        time_estimate = validated_data["time_estimate"]
        due_date = validated_data["due_date"]
        i = importance_calc(due_date, time_estimate)
        print(timezone.now())
        docket = Task(
            importance=i[0],
            daily_time_amount=i[1],
            name=validated_data["name"],
            time_estimate=time_estimate,
            due_date=due_date,
            docket=validated_data["docket"],
            done_today=False
        )
        docket.save()
        return docket


class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task


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


class DocketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docket
        exclude = ('user',)

    def create(self, validated_data):
        request = self.context.get('request')

        if request.user.sis_username and request.user.sis_password:
            dockets = []
            class_list = request_grades(request.user.sis_username,
                                        request.user.sis_password, False)
            for index, element in enumerate(class_list[1]):
                d = Docket(
                    name=class_list[0][index],
                    grade=class_list[1][index],
                    user=request.user
                )
                if len(Docket.objects.filter(user=request.user,
                                             name=class_list[0][index])) is 0:
                    d.save()
                    dockets.append(d)
            print(len(dockets))
            if len(dockets) is 0:
                raise ValidationError("You've done this before!")
            else:
                return dockets[0]
        else:
            docket = Docket(
                name=validated_data["name"],
                user=request.user
            )
            if len(Docket.objects.filter(user=request.user,
                                         name=docket.name)) is not 0:
                raise ValidationError("Already have that name")
            else:
                docket.save()
                return docket


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version

    def create(self, validated_data):
        request = self.context.get('request')
        if not request.user.is_staff:
            raise ValidationError("Only Admins can do this")
