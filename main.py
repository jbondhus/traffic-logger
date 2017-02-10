import logging.handlers
import traceback

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Config import Config
from Directions import Directions
from Models import *

my_logger = logging.getLogger('traffic-logger')
my_logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('logs/traffic-logger.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)

my_logger.addHandler(handler)

try:
    config = Config().get()

    engine = create_engine(config['sql_connection_string'])
    Session = sessionmaker(bind=engine)

    session = Session()

    api_key = config['google_api_key']

    forward_route_id = 1
    backward_route_id = 2

    forward_directions = Directions(session, api_key, forward_route_id)
    backward_directions = Directions(session, api_key, backward_route_id)

    my_logger.addHandler(handler)

    my_logger.info('Forward Seconds: ' + str(forward_directions.get_seconds()))
    my_logger.info('Backward Seconds: ' + str(backward_directions.get_seconds()))

    my_logger.debug('Inserting data')

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

    my_logger.debug('Inserted data')
except Exception as e:
    my_logger.error(str(e))
    my_logger.info(traceback.format_exc())
