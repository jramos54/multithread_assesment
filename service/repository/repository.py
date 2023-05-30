from service.model.message import Message
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker


class SensorRepository:
    '''
    it does the logic for the model
    '''
    def __init__(self) -> None:
        '''
        initialization of the class
        '''
        engine = create_engine("sqlite:///data.db")
        self.check_table_exist(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def check_table_exist(self, engine: any) -> None:
        '''
        check for the table if not exist it is created
        '''
        inspector = inspect(engine)
        if not inspector.has_table("messages"):
            self.create_table(engine)

    def create_table(self, engine: any) -> None:
        '''
        method for create the table
        '''
        Message.__table__.create(bind=engine)

    def save_to_database(self, sensor: any) -> None:
        '''
        method for save the data to db
        '''
        message = Message(
            timestamp=sensor.timestamp, sensor_name=sensor.name, value=sensor.value
        )
        self.session.add(message)
        self.commit()
