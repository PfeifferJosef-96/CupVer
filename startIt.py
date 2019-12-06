from sqlalchemy import create_engine

from cupver.comps.VrCup import VrCup
from cupver.DB.DB import Session

engine = create_engine("sqlite:///:newDB.sqlite", echo=True)

from cupver.DB.DB import Base




Session.configure(bind=engine)
session = Session()

Base.metadata.create_all(engine)
vr = VrCup()


vr.importParticipantsFromFile(session,'./Meldungen_Bsp.xlsx')
