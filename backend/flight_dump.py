import requests
import json
from flight import Flight

class Flight_Dump:

    @staticmethod
    def getFlightInfo(flight):
        flight_out = {}
        arrival_out = {}

        flight_out["air_code"] = flight.airline_code
        flight_out["air_name"] = flight.airline_name

        flight_out["port_code"] = flight.airport_code
        flight_out["port_name"] = flight.airport_name

        flight_out["fly_city"] = flight.flight_city
        flight_out["fly_gate"] = flight.flight_gate

        flight_out["fly_term"] = flight.flight_terminal
        flight_out["fly_delay"] = flight.flight_delay

        flight_out["fly_sched"] = flight.flight_schedule

        flight_out["fly_lat"] = flight.flight_lat
        flight_out["fly_lng"] = flight.flight_long

        flight_out["fly_num"] = flight.flight_num
        flight_out["fly_dist"] = flight.flight_distance

        arrival_out["air_code"] = flight.arrival.airline_code
        arrival_out["air_name"] = flight.arrival.airline_name

        arrival_out["port_code"] = flight.arrival.airport_code
        arrival_out["port_name"] = flight.arrival.airport_name

        arrival_out["fly_city"] = flight.arrival.flight_city
        arrival_out["fly_term"] = flight.arrival.flight_terminal

        arrival_out["fly_lat"] = flight.arrival.flight_lat
        arrival_out["fly_long"] = flight.arrival.flight_long

        arrival_out["fly_gate"] = flight.arrival.flight_gate

        flight_out["arrival"] = arrival_out

        return json.dumps(flight_out)
