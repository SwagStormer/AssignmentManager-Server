from rest_framework import viewsets
from serializers import AssignmentSerializer, AssignmentReadSerializer, ScheduleSerializer, MyUserSerializer, MyUserReadSerializer
from models import Assignment, Schedule, MyUser
# Create your views here.


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AssignmentSerializer
        else:
            return AssignmentReadSerializer

    def get_queryset(self):
        s = Schedule.objects.filter(user=self.request.user)
        return_array = []
        for schedule in s:
            return_array += Assignment.objects.filter(schedule=schedule)
        return return_array


class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    queryset = Schedule.objects.all()

    def get_queryset(self):
        return Schedule.objects.filter(user=self.request.user.id)


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

