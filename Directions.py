import json

import googlemaps
from datetime import datetime

from Location import Location
from Route import Route


class Directions:
    def __init__(self, session, api_key, route_id):
        route = Route(session, route_id)

        self.__start_location = Location(session, route.get_start_location())
        self.__end_location = Location(session, route.get_end_location())

        maps_client = googlemaps.Client(key=api_key)

        now = datetime.now()

        self.__directions_result = maps_client.directions(
            self.__start_location.get_full_address(),
            self.__end_location.get_full_address(),
            mode="driving",
            departure_time=now
        )[0]

    def get_directions_result(self):
        return self.__directions_result

    def get_seconds(self):
        return self.__directions_result['legs'][0]['duration']['value']

    def get_traffic_seconds(self):
        return self.__directions_result['legs'][0]['duration_in_traffic']['value']

    def get_all_data(self):
        return json.dumps(self.__directions_result)
