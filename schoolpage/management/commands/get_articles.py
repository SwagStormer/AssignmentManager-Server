from django.core.management.base import BaseCommand
from schoolpage.models import Announcement
from schoolpage.management.commands.announcement_scraper import get_announcements


class Command(BaseCommand):
    help = "Update the list of needed items on the todo list"

    def handle(self, *args, **options):
        for announcement in get_announcements():
            if len(Announcement.objects.filter(header=announcement.header, content=announcement.content)) is 0:
                announcement.save()
        self.stdout.write("Done!")
