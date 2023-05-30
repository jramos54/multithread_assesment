import datetime

from sensor.base_sensor import Sensor


class LoggingService:
    """
    it creates the logging service which collects the timestamp
    for each sensor
    """

    def get_timestamp(self) -> datetime.datetime:
        """function which capture the timestamp"""
        return datetime.datetime.now()

    def log_sensor_data(self, sensor: Sensor):
        """function which print the log into the screen"""
        timestamp = self.get_timestamp()
        log_data = f"Timestamp: {timestamp}, Sensor:{sensor.name}, value:{sensor.value}"
        print(log_data)
