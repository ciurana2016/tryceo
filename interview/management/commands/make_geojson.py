from django.core.management.base import BaseCommand

from interview.geojson import make_geojson_file
from interview.models import CountryArea



class Command(BaseCommand):

    """
        Generate geojson files
    """

    def handle(self, *args, **options):
        print('[Make geojson] START')

        for area in CountryArea.objects.all():
            make_geojson_file(area)

        print('[Make geojson] END')
