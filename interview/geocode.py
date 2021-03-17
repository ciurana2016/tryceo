from interview.models import Hotel
import json
import time
import requests

from random import choice
from .models import Hotel



def geocode_address(address:str) -> dict:
    """
    Call the API
    """
    url = 'http://api.positionstack.com/v1/forward'
    payload = {
        'access_key': 'b477fd54ae6201d9cd4ee3cfe0a934a7',
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


def update_hotel_geodata(hotel: Hotel):
    """
    Populates latitude and longitude fields
    """

    geo_data = geocode_address(hotel.address)
    if geo_data['ok']:
        hotel.latitude = geo_data['latitude']
        hotel.longitude = geo_data['longitude']
        hotel.save()
    else:
        print('! Error with the request')
