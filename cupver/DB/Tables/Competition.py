from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from cupver.DB.DB import Base


class Competition(Base):

    ___tablename__ = "competitions"

    id = Column(Integer, primary_key=True)
    town = Column(String)
    date = Column(String)
    nr = Column(Integer)

