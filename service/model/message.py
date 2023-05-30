from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Message(Base):
    """
    model using SQLalchemy
    """

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    sensor_name = Column(String)
    value = Column(Integer)
