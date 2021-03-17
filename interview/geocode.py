from interview.models import Hotel
import json
import time
import requests

from random import choice
from .models import Hotel



def geocode_address(address:str) -> dict:
    """
    Did not found a good free API without needing to make an account,
    so we are exploting this page.
    """
    url = 'https://positionstack.com/geo_api.php'
    payload = {'query': address}
    r = requests.get(url, params=payload)

    if (status := r.status_code == 200):
        data = json.loads(r.text)
        return  {
            'latitude': data['data'][0]['latitude'],
            'longitude': data['data'][0]['longitude'],
            'ok':  status
        }
    else:
        return {'ok': status}


def update_hotel_geodata(hotel: Hotel):
    """
    Populates latitude and longitude fields
    """

    # Make semi random sleeps
    time.sleep(choice([.1,.1,.1,.1,.2,.2,.3,.4]))

    geo_data = geocode_address(hotel.address)
    if geo_data['ok']:
        hotel.latitude = geo_data['latitude']
        hotel.longitude = geo_data['longitude']
        hotel.save()
    else:
        print('! Error with the request')
