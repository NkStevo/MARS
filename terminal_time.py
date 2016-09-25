import requests
import json
from flight import Flight

class Terminal_Time:

    @staticmethod
    def terminalWaitList(flight):
        a_code = flight.airport_code
        airline = flight.airline_name

        payload = {'airport': a_code, 'apikey': 'N8asxYvgleOXWqX5QcUsn19bmR7ysTN7'}
        a = requests.get('https://demo30-test.apigee.net/v1/hack/tsa', params=payload)
        json_output = a.json()

        wait_list = {}

        for s in json_output["AirportResult"][0]["airport"]["checkpoints"]:
            for j in s["precheckCarriers"]:
                if airline in j["name"]:
                    wait_list[s["id"]] = "none"

        for s in json_output["WaitTimeResult"]:
            if wait_list.has_key(s["checkpointID"]) and wait_list[s["checkpointID"]] is "none":
                wait_list[s["checkpointID"]]=s["waitTime"]

        return json.dumps(wait_list)
