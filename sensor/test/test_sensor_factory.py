from sensor.sensor_factory import SensorFactory


def test_create_sensor():
    sensor_factory = SensorFactory()
    sensor = sensor_factory.create_sensor("Sensor 1", "2021-01-01 00:00:00")
    assert sensor.name == "Sensor 1"
    assert isinstance(sensor.value, int)
    assert sensor.timestamp == "2021-01-01 00:00:00"


def test_random_values():
    sensor_factory = SensorFactory()

    # Crear múltiples sensores y verificar que los valores sean aleatorios dentro del rango especificado
    for _ in range(10):
        sensor = sensor_factory.create_sensor("Sensor", "2021-01-01 00:00:00")
        assert -100 <= sensor.value <= 100
