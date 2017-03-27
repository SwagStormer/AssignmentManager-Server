from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed, HttpResponse, HttpResponseBadRequest, Http404
from datetime import datetime
from rest_framework.exceptions import ValidationError, NotAuthenticated
import json
from .serializers import TaskSerializer, TaskReadSerializer, CourseSerializer, MyUserSerializer, MyUserReadSerializer, VersionSerializer
from .models import Course, Task, MyUser, Version
from assignment.management.commands.update_grades import update_or_create_grades
from django.shortcuts import get_object_or_404
# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @detail_route(methods=["POST"])
    def finish(self, request, pk=None):
        task = get_object_or_404(Task.objects.filter(id=pk))
        try:
            print()
            course = Course.objects.filter(user=request.user, id=task.course.id)[0]
        except IndexError:
            return Response(status=401)
        task.is_finished = True
        task.save()
        return HttpResponse(status=200)

    @detail_route(methods=["POST"])
    def snooze(self, request, pk=None):
        task = get_object_or_404(Task.objects.filter(id=pk))
        try:
            course = Course.objects.filter(user=request.user, id=task.course.id)[0]
        except IndexError:
            return Response(status=401)
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            content = body['snooze_until']
            task.snooze_until = content
        except KeyError:
            return HttpResponseBadRequest("Your json is funky. plz fix")
        task.save()
        return HttpResponse(status=200)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return TaskSerializer
        else:
            return TaskReadSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            courses = Course.objects.filter(user=self.request.user.id)
            return Task.objects.filter(course=courses, is_finished=False)
        else:
            return Task.objects.none()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @list_route(methods=["POST"])
    def update_grades(self, request):
        courses = Course.objects.filter(user=request.user.id)
        serializer = self.get_serializer(courses, many=True)
        update_or_create_grades(request.user)
        return Response(serializer.data)

    def get_queryset(self):
        return Course.objects.filter(user=self.request.user.id)


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
