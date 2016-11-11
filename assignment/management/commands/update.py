from django.core.management.base import BaseCommand
from assignment.models import Task
from assignment.importance import importance_calc


class Command(BaseCommand):
    help = "Update the list of needed items on the todo list"

    def handle(self, *args, **options):
        for task in Task.objects.all():
            if task.time_estimate is 0:
                task.delete()
            else:
                if task.done_today:
                    task.done_today = False
                else:
                    i = importance_calc(task.due_date, task.time_estimate)
                    task.importance = i[0]
                    task.daily_time_amount = i[1]
                task.save()
        self.stdout.write("Done!")
