from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from cupver.DB.DB import Base


class CompetitionData(Base):

    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True)
    town = Column(String)
    date = Column(String)
    nr = Column(Integer)

    #results = relationship("Result", back_populates="competition_id")

