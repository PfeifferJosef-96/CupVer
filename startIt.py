import pandas as pd
from sqlalchemy import create_engine

from cupver.comps.VrCup import VrCup
from cupver.DB.DB import Base, Session

engine = create_engine("sqlite:///:newDB.sqlite", echo=True)



Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)
vr = VrCup()

vr.connectToDatabase(session)

vr.importParticipantsFromFile(session, "./Meldungen_Bsp.xlsx")

print(vr.getAllParticipants())


cols = ["Rang", "Name", "Info"]
df = pd.read_excel("ErgebnisTest_OnTime.xlsx")

compInfoDict = {
    "resultData": df,
    "compData": {"nr": 1, "town": "Reit im Winkl", "date": "19.02.1999"},
}
vr.addNewCompetition(compInfoDict)
