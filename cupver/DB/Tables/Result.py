from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cupver.DB.DB import Base


class Result(Base):

    __tablename__ = "results"

    resultId = Column(Integer, primary_key=True)
    rank = Column(Integer)
    runTime = Column(String)
    points = Column(Integer)

    def getId(self):

        return self.resultId

