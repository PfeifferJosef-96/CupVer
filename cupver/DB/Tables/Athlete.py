from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from cupver.DB.DB import Base


class Athlete(Base):

    __tablename__ = "athletes"

    athleteId = Column(Integer, primary_key=True)
    name = Column(String)
    firstName = Column(String)
    classGroup = Column(String)
    birthYear = Column(Integer)
    sex = Column(String)
    club = Column(String)

    def getId(self):

        return self.athleteId


class ResultAssociation(Base):

    __tablename__ = "resultAssociation"

    athleteId = Column(Integer, ForeignKey("athletes.athleteId"), primary_key=True)
    competitionNr = Column(
        Integer, ForeignKey("competitions.competitionNr"), primary_key=True
    )
    result = Column(Integer, ForeignKey("results.resultId"))
    #result = relationship("Result")

    def getId(self):

        return (self.athleteId, self.competitionNr)

