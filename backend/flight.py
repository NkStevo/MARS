import requests
import sys

class Flight:
    def __init__(self, flight_info):
        if len(flight_info) <= 2:
            payload = {'flightNumber': flight_info[0], 'flightOriginDate': flight_info[1], 'apikey': 'N8asxYvgleOXWqX5QcUsn19bmR7ysTN7'}
            r = requests.get('https://demo30-test.apigee.net/v1/hack/status', params=payload)
            json_output = r.json()

            self.airline_code = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["airlineCode"]
            self.airline_name = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["airlineName"]
            self.airport_code = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureAirportCode"]
            self.airport_name = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureAirportName"]

            self.flight_city = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureCityName"]

            try:
                self.flight_gate = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureGate"]
            except KeyError:
                self.flight_gate = 'gate not yet assigned'

            self.flight_terminal = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureTerminal"]

            self.flight_delay = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureLocalTimeEstimatedActualString"]
            self.flight_schedule = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureLocalTimeScheduled"]

            self.flight_lat = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureTsoagLatitudeDecimal"]
            self.flight_long = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["departureTsoagLongitudeDecimal"]

            self.flight_num = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["flightNumber"]
            self.flight_distance = json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["flightDistance"]

            arrival_vars = [
                self.airline_code,
                self.airline_name,

                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalAirportCode"],
                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalAirportName"],

                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalCityName"],
                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalTerminal"],

                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLatitudeDecimal"],
                json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalTsoagLongitudeDecimal"]
            ]

            try:
                arrival_vars.insert(json_output["flightStatusResponse"]["statusResponse"]["flightStatusTO"]["flightStatusLegTOList"]["arrivalGate"], 3)
            except KeyError:
                arrival_vars.append('gate not yet assigned')

            self.arrival = Flight(arrival_vars)
        else:
            self.airline_code = flight_info[0]
            self.airline_name = flight_info[1]

            print flight_info

            self.airport_code = flight_info[2]
            self.airport_name = flight_info[3]

            self.flight_city = flight_info[4]

            self.flight_terminal = flight_info[5]

            self.flight_lat = flight_info[6]
            self.flight_long = flight_info[7]

            self.flight_gate = flight_info[8]
