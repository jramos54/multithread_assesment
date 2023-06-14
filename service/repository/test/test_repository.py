import os
from service.repository.repository import SensorRepository
from service.model.message import Message


def test_check_table_exist():
    repository = SensorRepository()

    # Verificar que la tabla no existe inicialmente
    assert not repository.engine.has_table("messages")

    # Ejecutar el método check_table_exist()
    repository.check_table_exist(repository.engine)

    # Verificar que la tabla se haya creado
    assert repository.engine.has_table("messages")


def test_create_table():
    repository = SensorRepository()

    # Verificar que la tabla no existe inicialmente
    assert not repository.engine.has_table("messages")

    # Ejecutar el método create_table()
    repository.create_table(repository.engine)

    # Verificar que la tabla se haya creado
    assert repository.engine.has_table("messages")


def test_save_to_database():
    repository = SensorRepository()

    # Crear un objeto Sensor para guardar en la base de datos
    timestamp = "2021-01-01 00:00:00"
    sensor_name = "Sensor 1"
    value = 10
    sensor = Message(timestamp=timestamp, sensor_name=sensor_name, value=value)

    # Guardar el sensor en la base de datos
    repository.save_to_database(sensor)

    # Verificar que el sensor se haya guardado correctamente
    saved_sensor = repository.session.query(Message).filter_by(sensor_name=sensor_name).first()
    assert saved_sensor is not None
    assert saved_sensor.timestamp == timestamp
    assert saved_sensor.sensor_name == sensor_name
    assert saved_sensor.value == value

    # Limpiar la base de datos eliminando el sensor guardado
    repository.session.delete(saved_sensor)
    repository.commit()


def teardown_module():
    # Eliminar el archivo de la base de datos después de ejecutar los casos de prueba
    os.remove("data.db")
