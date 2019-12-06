from sqlalchemy import Column, Integer, String

from cupver.DB.DB import Base


class Athlete(Base):

    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    firstName = Column(String)
    classGroup = Column(String)
    birthYear = Column(Integer)
    sex = Column(String)
    club = Column(String)
