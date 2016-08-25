from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from importance import importance_calc
from rest_framework.exceptions import ValidationError
from serializers import AssignmentSerializer, AssignmentReadSerializer, ScheduleSerializer, MyUserSerializer, MyUserReadSerializer
from models import Assignment, Schedule, MyUser
# Create your views here.


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    @detail_route(methods=["POST"])
    def done_today(self, request, pk=None):
        time_amount = request.data.get('time_amount')
        if not time_amount:
            if time_amount is not 0:
                raise ValidationError("Wai you do this")
        assignment = Assignment.objects.filter(id=pk)[0]

        if assignment.daily_time_amount is time_amount:
            assignment.time_estimate -= assignment.daily_time_amount
        elif assignment.time_estimate - time_amount is 0:
            assignment.delete()
            return Response(status=200)
        else:
            assignment.time_estimate -= time_amount
            i = importance_calc(assignment.due_date, assignment.time_estimate)
            assignment.daily_time_amount = i[1]
            assignment.importance = i[0]

        assignment.done_today = True
        assignment.save()
        return Response(status=200)

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AssignmentSerializer
        else:
            return AssignmentReadSerializer

    def get_queryset(self):
        s = Schedule.objects.filter(user=self.request.user)
        return_array = []
        for schedule in s:
            a = Assignment.objects.filter(schedule=schedule, done_today=False)
            return_array += a
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

