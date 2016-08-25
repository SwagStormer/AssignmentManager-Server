from django.core.management.base import BaseCommand
from assignment.models import Assignment


class Command(BaseCommand):
    help = "Update the list of needed items on the todo list"

    def handle(self, *args, **options):
        for assignment in Assignment.objects.all():
            if assignment.time_estimate is 0:
                assignment.delete()
            else:
                assignment.done_today = False
                assignment.save()
        self.stdout.write("Done!")