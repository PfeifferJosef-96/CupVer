import pandas as pd
from sqlalchemy import create_engine
from cupver.DB.Tables.Athlete import Athlete

from cupver.comps.VrCup import VrCup
from cupver.DB.DB import Base, Session
from cupver.io.Importer import OnTimeImporter
from cupver.io.Exporter import OnTimeExporter

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


#compInfoDict = dict(competitionNr=2, town="Reit im Winkl", date="19.02.1999", discName="donotknow")


#vr.addNewCompetition(compInfoDict)

#for itDat  in resData:
#    vr.addNewResult(itDat,2)

exporter = OnTimeExporter()

df = vr.getAllParticipants()

exporter.exportDataFrameToFile(df, 'onTimeExport.xls')

vr.exportAthletesToOnTime()

