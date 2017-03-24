from django.core.management import BaseCommand

from assignment.models import MyUser, Course
from assignment.scraper import request_grades


def update_or_create_grades(user):
    grades = request_grades(user.sis_username, user.sis_password, False)
    for index, element in enumerate(grades[1]):

        try:
            course = Course.objects.filter(name=grades[0][index], user=user.id)[0]
            course.grade = grades[1][index]
        except IndexError:
            course = Course(grade=grades[1][index], name=grades[0][index], user=user)

        course.save()


class Command(BaseCommand):

    help = "Update grades"

    def handle(self, *args, **options):
        users = MyUser.objects.all()

        for user in users:
            update_or_create_grades(user)

        self.stdout.write('Finished!')