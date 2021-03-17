from django.core.management.base import BaseCommand

from interview.geocode import Geocoder



class Command(BaseCommand):

    """
        Bulk update geocode to all hotels
    """

    def handle(self, *args, **options):
        print('[Update hotel geodata] START')

        # Call object

        print('[Update hotel geodata] END')
