import random
import time
from threading import Thread

from utils import network
from logging_service.logging_service import LoggingService
from sensor.sensor_factory import SensorFactory
from service.model.message import Message
from service.repository.repository import SensorRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

def simulate_sensor(sensor, logging_service, network_obj):
    '''
    Creates the sensor simulation
    '''
    with network_obj.semaphore:

        engine = create_engine("sqlite:///data.db")
        session_factory = sessionmaker(bind=engine)
        Session = scoped_session(session_factory)

        session = Session()
        while True:
            timestamp = logging_service.get_timestamp()
            sensor.timestamp = timestamp
            logging_service.log_sensor_data(sensor)
            message = Message(
                timestamp=sensor.timestamp, sensor_name=sensor.name, value=sensor.value
            )
            session.add(message)
            session.commit()
            # Each sensor has its own delay
            time.sleep(sensor.delay)

        session.remove()


def simulate_sensor_logging():
    '''
    Creates the threading and runs the simulation
    '''
    sensor_factory = SensorFactory()
    logging_service = LoggingService()

    sensor_specs = [
        {"name": "Sensor 1", "delay": random.uniform(1, 10)},
        {"name": "Sensor 2", "delay": random.uniform(1, 10)},
        {"name": "Sensor 3", "delay": random.uniform(1, 10)},
        {"name": "Sensor 4", "delay": random.uniform(1, 10)},
        {"name": "Sensor 5", "delay": random.uniform(1, 10)},
        {"name": "Sensor 6", "delay": random.uniform(1, 10)},
        {"name": "Sensor 7", "delay": random.uniform(1, 10)},
        {"name": "Sensor 8", "delay": random.uniform(1, 10)},
        {"name": "Sensor 9", "delay": random.uniform(1, 10)},
        {"name": "Sensor 10", "delay": random.uniform(1, 10)},
    ]

    network_obj = network.Network()
    threads = []

    for spec in sensor_specs:
        sensor = sensor_factory.create_sensor(spec["name"], "")
        sensor.delay = spec["delay"]
        thread = Thread(
            target=simulate_sensor, args=(sensor, logging_service, network_obj)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    repository = SensorRepository()
    simulate_sensor_logging()
