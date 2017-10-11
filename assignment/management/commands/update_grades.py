from django.core.management import BaseCommand

from assignment.models import MyUser, Course
from assignment.scraper import request_grades


def update_or_create_grades(user):
    grades = request_grades(user.sis_username, user.sis_password, False)
    for grade in grades:
        course = Course.objects.filter(name=grade.course_name,
                                       user=user.id).first()
        if course is None:
            course = Course(grade=grade.grade, name=grade.course_name, user=user)
        else:
            course.grade = grade.grade
        course.save()


class Command(BaseCommand):

    help = "Update grades"

    def handle(self, *args, **options):
        users = MyUser.objects.all()

        for user in users:
            update_or_create_grades(user)

        self.stdout.write('Finished!')
