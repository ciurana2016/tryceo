import json

from app.settings import STATICFILES_DIRS
from .models import CountryArea, Hotel


class MapBoundingBox(object):
    '''
        TODO Tests
        This class can iterate longitud and latitude points to create a box
        defining the bounding box of a CountryArea
    '''

    def __init__(self):
        self.p1_lon, self.p1_lat = False, False
        self.p2_lon, self.p2_lat = False, False
        self.first_point = False

    def fits_spain(self, hotel: Hotel) -> bool:
        # Our geolocation api was fucked so we have to fit the points
        # to spain [top_left [long, lat], bottom_right [long, lat]]
        spain = [
            [-8.804037, 44.213710],
            [3.427445, 35.421371]
        ]

        false_long = hotel.longitude < spain[0][0] or \
            hotel.longitude > spain[1][0]
        false_lat = hotel.latitude > spain[0][1] or \
            hotel.latitude < spain[1][1]

        if false_long or false_lat:
            return False
        else:
            return True

    def fit_hotel_points(self, hotel: Hotel) -> bool:
        # Filter bad results
        if hotel.latitude == None or hotel.longitude == None:
            return False

        # Not a spain point
        if not self.fits_spain(hotel):
            return False

        # First points of box
        if self.first_point == False:
            self.p1_lon = hotel.longitude
            self.p1_lat = hotel.latitude
            self.p2_lon = hotel.longitude
            self.p2_lat = hotel.latitude
            self.first_point = True
            return True

        # Now we chech every point
        if hotel.latitude > self.p1_lat:
            self.p1_lat = hotel.latitude
        if hotel.longitude < self.p1_lon:
            self.p1_lon = hotel.longitude

        if hotel.latitude < self.p2_lat:
            self.p2_lat = hotel.latitude
        if hotel.longitude > self.p2_lon:
            self.p2_lon = hotel.longitude

        return True

    def get_box(self) -> list:
        return [
            [float(self.p1_lon), float(self.p1_lat)],
            [float(self.p2_lon), float(self.p2_lat)]
        ]


def make_geojson_file(country_area: CountryArea) -> None:
    """
        TODO Tests
        This function makes 2 things at once:
        1. Generate the geojson file for a given CountryArea
        2. Calculate the bounding box points of the CountryArea and save it
    """

    # Bounding box calculations
    MapBox = MapBoundingBox()

    # Dict to be converted to geojson
    data = {
        'type': 'FeatureCollection',
        'crs': {
            'type': 'name', 'properties': {
                'name': 'urn:ogc:def:crs:OGC:1.3:CRS84'
            }
        },
        'features': []
    }

    for hotel in Hotel.objects.filter(country_area=country_area):
        # Fit bounding box
        # fit_hotel returs false if it was not in spain
        # our geoapi geocoded a bunch of bad results
        if MapBox.fit_hotel_points(hotel):
            data['features'].append({
                'type': 'Feature',
                'properties': {
                    'name': hotel.name,
                    'url': hotel.url,
                    'area': country_area.name,
                    'address': hotel.address
                },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [float(hotel.longitude), float(hotel.latitude)]
                }
            })

    # Save area bounding box
    country_area.bounding_box = str(MapBox.get_box())

    # Save geojson file
    file_path = str(STATICFILES_DIRS[0]) + '/geojson/'
    file_name = f'{country_area.name.replace(" ", "")}.geojson'

    with open(file_path + file_name, 'w') as f:
        json.dump(data, f)
