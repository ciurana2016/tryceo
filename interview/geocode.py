import json
import requests



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
