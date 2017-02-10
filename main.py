from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from Config import Config
from Directions import Directions
from Models import *

Base = automap_base()

config = Config().get()

engine = create_engine(config['sql_connection_string'])
Session = sessionmaker(bind=engine)

session = Session()

api_key = config['google_api_key']

forward_route_id = 1
backward_route_id = 2

forward_directions = Directions(session, api_key, forward_route_id)
backward_directions = Directions(session, api_key, backward_route_id)

print('Forward: ' + str(forward_directions.get_traffic_seconds()))
print('Backward: ' + str(backward_directions.get_traffic_seconds()))

print('Inserting data...')

session.add_all(
    [
        Transit(
            route_id=forward_route_id,
            duration=forward_directions.get_seconds(),
            all_data=forward_directions.get_all_data()
        ),
        Transit(
            route_id=backward_route_id,
            duration=backward_directions.get_seconds(),
            all_data=backward_directions.get_all_data()
        )
    ]
)

session.commit()

print('Inserted data')
