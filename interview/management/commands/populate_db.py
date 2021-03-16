from django.core.management.base import BaseCommand

from interview.database import filter_and_save_data



class Command(BaseCommand):

    """
        Populates the Django models with data from the remote database.
    """

    def handle(self, *args, **options):
        print('[Populate db] START')
        filter_and_save_data()
        print('[Populate db] END')
