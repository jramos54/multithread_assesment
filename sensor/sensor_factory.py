import random

from sensor.base_sensor import Sensor


class SensorFactory:
    """
    it implements the factory pattern for sensors
    """

    def create_sensor(self, name: str, timestamp: str) -> Sensor:
        '''
        it creates the sensor
        '''
        value = random.randint(-100, 100)
        return Sensor(name=name, value=value, timestamp=timestamp)
    
    