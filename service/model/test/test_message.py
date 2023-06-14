from service.model.message import Message


def test_message_creation():
    timestamp = "2021-01-01 00:00:00"
    sensor_name = "Sensor 1"
    value = 10

    message = Message(timestamp=timestamp, sensor_name=sensor_name, value=value)

    assert message.timestamp == timestamp
    assert message.sensor_name == sensor_name
    assert message.value == value


def test_message_equality():
    timestamp = "2021-01-01 00:00:00"
    sensor_name = "Sensor 1"
    value = 10

    message1 = Message(timestamp=timestamp, sensor_name=sensor_name, value=value)
    message2 = Message(timestamp=timestamp, sensor_name=sensor_name, value=value)
    message3 = Message(timestamp="2022-01-01 00:00:00", sensor_name=sensor_name, value=value)

    assert message1 == message2
    assert message1 != message3
