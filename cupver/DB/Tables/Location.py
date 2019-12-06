from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from cupver.DB.DB import Base


class Location(Base):

    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    town = Column(String)
    date = Column(String)

