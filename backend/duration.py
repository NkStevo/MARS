import requests
from app import app
from flight import Flight

class Duration:

    @staticmethod
    def getDriveTime(flight):
        flight = Flight(['2203', '2016-09-26'])

        #places_resp = requests.get(gp_url)


        #gp_payload = {'key':'google_places_api_key','location':location,'radius':'100','rankby':'distance'}
        #places_resp = requests.get(gp_url,params=gp_payload)

        f = requests.get('http://freegeoip.net/json/')

        location = f.json()

        location_city = location['city']
        location_region = location['region_name']
        location_country = location['country_name']

        location_longitude = location['longitude']
        location_latitude = location['latitude']

        gd_payload = 'origins=' + str(location_latitude) + "," + str(location_longitude) + \
            '&destinations=' + str(flight.flight_lat) + "," + str(flight.flight_long) + \
            '&traffic_model=' + 'optimistic' + '&departure_time=' + 'now'

        gd = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?' + gd_payload)
        duration_json = gd.json()

        return duration_json["rows"][0]["elements"][0]["duration"]["text"]
