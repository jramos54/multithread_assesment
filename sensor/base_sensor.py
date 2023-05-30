from dataclasses import dataclass


@dataclass
class Sensor:
    """To create an the sensor class as domain
    this class requiere:
                name as name of sensor
                value as sensor value
                timestamp as time when sensor work
    """

    name: str
    value: int
    timestamp: str
