from sqlalchemy import Column, Integer, BigInteger, ForeignKey, Unicode, Time, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, deferred

Base = declarative_base()


class State(Base):
    __tablename__ = "states"
    id = Column('state_id', Integer, primary_key=True, autoincrement=True)
    abbreviation = Column('state_abbreviation', Unicode)
    name = Column('state_name', Unicode)

    cities = relationship("City", back_populates="state")

    def __repr__(self):
        return '<State %s - %s>' % (self.id, self.abbreviation)


class City(Base):
    __tablename__ = "cities"
    id = Column('city_id', Integer, primary_key=True, autoincrement=True)
    name = Column('city_name', Unicode)
    state_id = Column('state', Integer, ForeignKey('states.state_id'))

    state = relationship('State', foreign_keys=state_id, back_populates="cities")
    locations = relationship('Location', back_populates="city")

    def __repr__(self):
        return '<City %r - %s, %s>' % (self.id, self.name, self.state.abbreviation)


class Location(Base):
    __tablename__ = "locations"
    id = Column('location_id', Integer, primary_key=True, autoincrement=True)
    address_1 = Column('address_1', Unicode)
    address_2 = Column('address_2', Unicode)
    city_id = Column('city', Integer, ForeignKey('cities.city_id'))
    latitude = Column('latitude', BigInteger)
    longitude = Column('longitude', BigInteger)

    city = relationship('City', foreign_keys=city_id, back_populates="locations")

    def __repr__(self):
        return '<Location %s>' % self.id


class Transit(Base):
    __tablename__ = "transit"
    transit_id = Column('transit_id', Integer, primary_key=True, autoincrement=True)
    route_id = Column('route', Integer, ForeignKey('routes.route_id'))
    duration = Column('duration', Integer)
    all_data = deferred(Column('all_data', Text))
    created_at = Column('created_at', Time)

    route = relationship('Route', foreign_keys=route_id, back_populates="transit")


class Route(Base):
    __tablename__ = "routes"
    id = Column('route_id', Integer, primary_key=True, autoincrement=True)
    start_location = Column('start_location', Integer, ForeignKey('locations.location_id'))
    end_location = Column('end_location', Integer, ForeignKey('locations.location_id'))

    transit = relationship('Transit', back_populates="route")
