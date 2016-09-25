import requests
from flight import Flight
from place import Place

class Places_Integration:

    @staticmethod
    def placeList(flight, keyword):
        #flight = Flight(['2203', '2016-09-26'])

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

        return places
