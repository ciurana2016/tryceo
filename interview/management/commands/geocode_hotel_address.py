from django.core.management.base import BaseCommand

from interview.geocode import update_hotel_geodata
from interview.models import Hotel


class Command(BaseCommand):

    """
        Loops all the hotels updating latitude and longitude
    """

    def handle(self, *args, **options):
        print('[Update hotel geodata] START')

        for idx, hotel in enumerate(Hotel.objects.all()):
            print(f'\t updating hotel {idx} ...')
            update_hotel_geodata(hotel)

        print('[Update hotel geodata] END')
