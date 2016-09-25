import requests
import flask
import json
from app import app
from flight import Flight

class Weather_Info:

    @staticmethod
    def getWeather(flight):

        a_code = flight.airport_code

        payload = {'code': a_code, 'apikey': 'N8asxYvgleOXWqX5QcUsn19bmR7ysTN7'}

        a = requests.get('https://demo30-test.apigee.net/v1/hack/weather', \
            params=payload)

        weather_json = a.json()

        weather_out = {}

        weather_out["temp"] = weather_json["condition"]["temp"]
        weather_out["desc"] = weather_json["condition"]["text"]

        return json.dumps(weather_out)
