from cupver.comps.Competition import Competition
from cupver.ImportParticipants import ImportParticipants
from cupver.DB.Tables.Athlete import Athlete
from cupver.DB.Tables.Location import Location


class VrCup(Competition):
    def __init__(self):

        ParticipantImport = ImportParticipants
        super(VrCup, self).__init__(
            ParticipantImport=ParticipantImport, Athlete=Athlete, Location=Location
        )

