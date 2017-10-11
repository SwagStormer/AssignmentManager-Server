from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (TaskSerializer, TaskReadSerializer, CourseSerializer,
                          MyUserSerializer, MyUserReadSerializer,
                          VersionSerializer)
from .models import Course, Task, MyUser, Version
from assignment.management.commands.update_grades import update_or_create_grades
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskSerializer
        else:
            return TaskReadSerializer

    def get_queryset(self):
        courses = Course.objects.filter(user=self.request.user)
        return Task.objects.filter(course__in=courses, is_finished=False)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        request = self.request
        q = self.request.query_params.get
        queryset = Course.objects.filter(user=self.request.user.id)
        if q("cached") == "false":
            update_or_create_grades(request.user)
        return queryset


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
