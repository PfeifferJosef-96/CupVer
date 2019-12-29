from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from cupver.DB.DB import Base


class CompetitionData(Base):

    __tablename__ = "competitions"

    #competitionId = Column(Integer, primary_key=True, autoincrement=True)
    competitionNr = Column(Integer, primary_key=True)
    town = Column(String)
    date = Column(String)
    discName = Column(String)

    def getId(self):
        return self.competitionNr
