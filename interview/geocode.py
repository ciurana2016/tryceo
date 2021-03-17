from interview.models import Hotel
import json
import requests

from .models import Hotel



class Geocoder(object):

    API_KEY = 'b477fd54ae6201d9cd4ee3cfe0a934a7'
    API_URL = 'http://api.positionstack.com/v1/forward'

    def __init__(self):
        pass

    def bulk_update(self):
        # Update geodata for all hotels (country:ESP)

        # Make a json object that the api can read with all the hotels
        batch_data = {'batch':[]}
        for hotel in Hotel.objects.all():
            batch_data['batch'].append({
                'query': hotel.address,
                'country': 'ES'
            })

        # Make the request
        payload = {
            'access_key': self.API_KEY,
        }
        r = requests.post(self.API_URL, params=payload, json=batch_data)
        print(r.status_code)
        print(r.text)


    def geocode_address(self, address:str) -> dict:
        # Geocode a single address
        payload = {
            'access_key': self.API_KEY,
            'query': address
        }
        r = requests.get(self.API_URL, params=payload)

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


