from django.core.management.base import BaseCommand

from interview.geocode import Geocoder
from interview.models import Hotel


class Command(BaseCommand):

    """
        Bulk update geocode to all hotels
    """

    def handle(self, *args, **options):
        print('[Update hotel geodata] START')

        for idx, hotel in enumerate(Hotel.objects.all()):
            print(f'\t updating hotel {idx} ...')
            Geocoder.update_hotel_geodata(hotel)

        print('[Update hotel geodata] END')
