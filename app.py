from requests import Request, Session, Response

def get_weather(lat, lon, key):
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

lat = 37.566535
lon = 126.9779692
key = '7fbae86e8ab4bd446287269c36407903'
print(get_weather(lat,lon,key))