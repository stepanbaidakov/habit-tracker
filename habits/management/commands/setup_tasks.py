from django.core.management.base import BaseCommand

from habits.services import create_periodic_tasks_for_habits


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        create_periodic_tasks_for_habits()
