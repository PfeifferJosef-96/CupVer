import pandas as pd
from sqlalchemy import create_engine
from cupver.DB.Tables.Athlete import Athlete

from cupver.comps.VrCup import VrCup
from cupver.DB.DB import Base, Session
from cupver.io.Importer import OnTimeImporter

engine = create_engine("sqlite:///:newDB.sqlite", echo=True)



Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)
vr = VrCup()

vr.connectToDatabase(session)

vr.importParticipantsFromFile(session, "./Meldungen_Bsp.xlsx")

print(vr.getAllParticipants())


imp = OnTimeImporter()

resData = imp.importResultFile("ErgebnisTest_OnTime.xlsx")


compInfoDict = {
    "resultData": resData,
    "compData": {"nr": 1, "town": "Reit im Winkl", "date": "19.02.1999"},
}
vr.addNewCompetition(compInfoDict)


