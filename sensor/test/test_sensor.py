from sensor.base_sensor import Sensor


def test_sensor_creation():
    sensor = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")
    assert sensor.name == "Sensor 1"
    assert sensor.value == 10
    assert sensor.timestamp == "2021-01-01 00:00:00"


def test_sensor_equality():
    sensor1 = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")
    sensor2 = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")
    assert sensor1 == sensor2


def test_sensor_inequality():
    sensor1 = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")
    sensor2 = Sensor(name="Sensor 2", value=20, timestamp="2022-02-02 12:00:00")
    assert sensor1 != sensor2


def test_immutable_attributes():
    sensor = Sensor(name="Sensor 1", value=10, timestamp="2021-01-01 00:00:00")
    # Intentamos modificar los atributos después de la creación
    sensor.name = "Sensor 2"
    sensor.value = 20
    sensor.timestamp = "2022-02-02 12:00:00"
    # Verificamos que los atributos no se hayan modificado
    assert sensor.name == "Sensor 1"
    assert sensor.value == 10
    assert sensor.timestamp == "2021-01-01 00:00:00"
