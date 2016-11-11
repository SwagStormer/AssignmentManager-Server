from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from importance import importance_calc
from rest_framework.exceptions import ValidationError
from serializers import TaskSerializer, TaskReadSerializer, DocketSerializer, MyUserSerializer, MyUserReadSerializer, VersionSerializer
from models import Docket, Task, MyUser, Version
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @detail_route(methods=["POST"])
    def done_today(self, request, pk=None):
        time_amount = request.data.get('time_amount')
        if not time_amount:
            if time_amount is not 0:
                raise ValidationError("Wai you do this")
        task = Task.objects.filter(id=pk)[0]
        if task.done_today:
            raise ValidationError("Task is finished for the day!")
        else:
            if task.daily_time_amount is time_amount:
                task.time_estimate -= task.daily_time_amount
            elif task.time_estimate - time_amount is 0:
                task.delete()
                return Response({"Status": "Deleted"}, status=200)
            else:
                task.time_estimate -= time_amount
                i = importance_calc(task.due_date, task.time_estimate)
                task.daily_time_amount = i[1]
                task.importance = i[0]

            task.done_today = True
            task.save()
            return Response({"Status": "Finished"}, status=200)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskSerializer
        else:
            return TaskReadSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous():
            return ValidationError("DERP")
        else:
            print(self.request.user)
            d = Docket.objects.filter(user=self.request.user)
            return_array = []
            for docket in d:
                a = Task.objects.filter(docket=docket, done_today=False)
                return_array += a
            return return_array


class DocketViewSet(viewsets.ModelViewSet):
    serializer_class = DocketSerializer
    queryset = Docket.objects.all()

    def get_queryset(self):
        return Docket.objects.filter(user=self.request.user.id)


class MyUserViewSet(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    queryset = MyUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MyUserSerializer
        else:
            return MyUserReadSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class VersionViewSet(viewsets.ModelViewSet):
    serializer_class = VersionSerializer
    queryset = Version.objects.all()
