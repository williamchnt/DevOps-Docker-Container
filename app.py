from requests import Request, Session, Response
import os

def get_weather(lat, lon, key):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'lat': lat,
            'lon': lon,
            'appid': key
        }
        s = Session()
        req = Request('GET', url, params=params)
        prepped = req.prepare()
        resp = s.send(prepped)
        return resp.json()
    except Exception as e:
        return e


lat = os.environ['LAT']
lon = os.environ['LONG']
key = os.environ['API_KEY']
print(get_weather(lat,lon,key))