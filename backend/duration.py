import requests
from app import app
from flight import Flight

flight = Flight(['1997', '2016-09-24'])

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

print gd_payload

url = 'http://maps.googleapis.com/maps/api/distancematrix/json?' + gd_payload
print url

gd = requests.get('http://maps.googleapis.com/maps/api/distancematrix/json?' + gd_payload)
duration_json = gd.json()
print duration_json["rows"][0]["elements"][0]["duration"]["text"]

#print r.url
#print location

#print response

#print lat_deg, long_deg
