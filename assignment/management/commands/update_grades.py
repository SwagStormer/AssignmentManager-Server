from django.core.management import BaseCommand

from assignment.models import MyUser, Course
from assignment.scraper import request_grades


def update_grades(user):
    grades = request_grades(user.sis_username, user.sis_password, False)
    for index, element in enumerate(grades[1]):
        course = Course.objects.filter(name=grades[0][index], user=user.id)[0]
        course.grade = grades[1][index]
        course.save()


class Command(BaseCommand):

    help = "Update grades"

    def handle(self, *args, **options):
        users = MyUser.objects.all()

        for user in users:
            update_grades(user)

        self.stdout.write('Finished!')