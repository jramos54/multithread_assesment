import datetime
from logging_service.logging_service import LoggingService
from sensor.base_sensor import Sensor
from io import StringIO
import sys


def test_get_timestamp():
    logging_service = LoggingService()
    timestamp = logging_service.get_timestamp()
    assert isinstance(timestamp, datetime.datetime)


def test_log_sensor_data(capsys):
    logging_service = LoggingService()
    sensor = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")

    logging_service.log_sensor_data(sensor)

    captured = capsys.readouterr()
    assert captured.out.strip() == "Timestamp: 2021-01-01 00:00:00, Sensor:Sensor 1, value:10"
