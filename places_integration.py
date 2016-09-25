import requests
import json
from flight import Flight
from place import Place

class Places_Integration:

    @staticmethod
    def placeList(flight, keyword):
        gd_payload = 'key=AIzaSyCQaKHt63pgkdx8v8p3PuhLDrFsvLGyMYM'+ \
            '&location=' + str(flight.arrival.flight_lat) + "," + \
            str(flight.arrival.flight_long) + '&radius=' + '32187'+ \
            '&keyword=' + keyword

        pl = requests.get( \
            'https://maps.googleapis.com/maps/api/place/nearbysearch/json?' + \
            gd_payload)

        places_json = pl.json()
        places = []

        for s in places_json["results"]:
            try:
                ph = s["photos"][0]["photo_reference"]
            except KeyError:
                ph = "none"

            pid = s["place_id"]
            places.append(Place(pid, ph))

        places_out = {'place_list': []}

        for s in places:
            places_out['place_list'].append({'name' : s.name, 'icon' : s.icon, \
                'rating' : s.rating, 'phone' : s.phone, 'address' : s.address, \
                'lat' : s.lat, 'lng' : s.lng})


        return json.dumps(places_out)
