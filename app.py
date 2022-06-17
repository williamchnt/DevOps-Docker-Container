from requests import Request, Session, Response
import os
from flask import Flask

app = Flask(__name__)

@app.route('/<lat>/<lon>')
def get_weather(lat, lon):
    try:
        key = os.environ['API_KEY']
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

if __name__ == "__main__":
       app.run(host='0.0.0.0',debug=True,port=8081)



# lat = os.environ['LAT']
# lon = os.environ['LONG']

# print(get_weather(lat,lon,key))