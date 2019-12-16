from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cupver.DB.DB import Base


class Result(Base):

    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    rank = Column(Integer)
    #competition_id = Column(Integer, ForeignKey("competitions.id"))
    athlete_id = Column(Integer, ForeignKey("athletes.id"))

    athlete = relationship("Athlete", back_populates="results")
