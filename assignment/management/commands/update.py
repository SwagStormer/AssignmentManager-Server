from django.core.management.base import BaseCommand
from assignment.models import Assignment
from assignment.importance import importance_calc


class Command(BaseCommand):
    help = "Update the list of needed items on the todo list"

    def handle(self, *args, **options):
        print(Assignment.objects.all())
        for assignment in Assignment.objects.all():
            if assignment.time_estimate is 0:
                assignment.delete()
            else:
                if assignment.done_today:
                    assignment.done_today = False
                else:
                    i = importance_calc(assignment.due_date, assignment.time_estimate)
                    assignment.importance = i[0]
                    assignment.daily_time_amount = i[1]
                assignment.save()
            print(assignment)
        self.stdout.write("Done!")
