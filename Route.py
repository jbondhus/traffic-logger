from Models import Route as RouteModel


class Route:
    def __init__(self, session, route_id):
        self.__session = session
        self.__route_id = route_id

        self.__route = session.query(RouteModel).filter_by(id=route_id).first()

        self.__start_location = self.__route.start_location
        self.__end_location = self.__route.end_location

    def get_start_location(self):
        return self.__start_location

    def get_end_location(self):
        return self.__end_location
