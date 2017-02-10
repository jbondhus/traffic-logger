from Models import Location as LocationModel


class Location:
    def __init__(self, session, location_id: object):
        self.__session = session
        self.__location_id = location_id

        self.__location = session.query(LocationModel).filter_by(id=location_id).first()

    def get_full_address(self) -> str:
        address = self.__location.address_1

        if self.__location.address_2 is not None:
            address += ' ' + self.__location.address_2

        address += ' ' + self.__location.city.name
        address += ', ' + self.__location.city.state.abbreviation

        return address
