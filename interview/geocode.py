from interview.models import Hotel
import json
import requests

from .models import Hotel



class Geocoder(object):

    API_KEY = 'b477fd54ae6201d9cd4ee3cfe0a934a7'

    def __init__(self):
        pass

    def geocode_address(self, address:str) -> dict:
        # Geocode a single address
        url = 'http://api.positionstack.com/v1/forward'
        payload = {
            'access_key': self.API_KEY,
            'query': address
        }
        r = requests.get(url, params=payload)

        if (status := r.status_code == 200):
            data = json.loads(r.text)
            try:
                return  {
                    'latitude': data['data'][0]['latitude'],
                    'longitude': data['data'][0]['longitude'],
                    'ok':  status
                }
            except:
                # The api fails sometimes lol
                pass

        return {'ok': False}

    def update_hotel_geodata(self, hotel: Hotel):
        # Updates latitude and longitude on single hotel
        geo_data = self.geocode_address(hotel.address)
        if geo_data['ok']:
            hotel.latitude = geo_data['latitude']
            hotel.longitude = geo_data['longitude']
            hotel.save()
        else:
            print('! Error with the request')


