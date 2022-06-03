from requests import Request, Session, Response

def get_weather(lat, lon):
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': '240aa650f4db4e154a07d0459c30a347'
    }
    s = Session()
    req = Request('GET', url, params=params)
    prepped = req.prepare()
    resp = s.send(prepped)
    return resp.json()

if __name__ == "__main__":
    lat = 37.566535
    lon = 126.9779692
    get_weather(lat,lon)