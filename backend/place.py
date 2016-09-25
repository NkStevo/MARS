import requests
import sys

class Place:
    def __init__(self, place_id, photo_ref):
        gd_payload = 'key=AIzaSyCQaKHt63pgkdx8v8p3PuhLDrFsvLGyMYM'+ \
            '&placeid=' + place_id

        pl = requests.get('https://maps.googleapis.com/maps/api/place/details/json?' + gd_payload)
        places_json = pl.json()

        print places_json

        self.name = places_json["result"]["name"]
        self.icon = places_json["result"]["icon"]

        try:
            self.rating = places_json["result"]["rating"]
        except KeyError:
            self.rating = "N/A"

        try:
            self.phone = places_json["result"]["formatted_phone_number"]
        except KeyError:
            self.phone = "N/A"

        self.address = places_json["result"]["formatted_address"]

        self.lat = places_json["result"]["geometry"]["location"]["lat"]
        self.lng = places_json["result"]["geometry"]["location"]["lng"]

        self.photo_ref = photo_ref
        #self.review_summary
