from cupver.DB.DB import DataInterface

from cupver.DB.Tables.Athlete import ResultAssociation


class Competition(object):
    def __init__(self, ParticipantImport, Athlete, ResultData, CompetitionData):

        self.ParticipantImport = ParticipantImport()
        self.Athlete = Athlete
        self.ResultData = ResultData
        self.CompetitionData = CompetitionData
        self.DataInterface = DataInterface()

    def getPartResult(self):
        raise NotImplementedError

    def getFinalResult(self):
        raise NotImplementedError

    def connectToDatabase(self, newSession):
        """Connect the Competition to a database.

        Args:
            newSession (sqlalchemy.Session): Session with engine

        Returns:
            status (int):   0 -> success
                            -1 -> error
        """

        status = self.DataInterface.connectToDatabase(newSession)

        return status

    def getAthleteByID(self, id):

        pass

    def addNewCompetition(self, compData):
        """
        """

        newComp = self.CompetitionData(**compData)
        compId = self.DataInterface.addNewTableEntry(newComp)

    def addNewResult(self, resultData, compId):
        """Add a new Result to a competition and
        connect it to an athlete.
        
        The result data format are a list of dicts. The key
        "id" in the result data is the athlete id. This will
        be converted to "athlete_id"

        Args:
            resultData (list(dict)): List with results

        Returns:
            resId (int): ID of the newly added result
        """

        athleteId = resultData.pop("athleteId")

        newRes = self.ResultData(**resultData)

        newAssoc = ResultAssociation(
            athleteId=athleteId, competitionNr=compId, result=None
        )

        id = self.DataInterface.addNewTableEntry(newAssoc)

        if id != -1:
            resId = self.DataInterface.addNewTableEntry(newRes, commitEntry=True)

            self.DataInterface.updateResultAssoc(athleteId, compId, resId)

        return resId

    def getAllParticipants(self):
        """
        """

        queryData = self.DataInterface.queryWholeTable(self.Athlete)

        return queryData

    def importParticipantsFromFile(self, session, fpath):
        """Participants are loaded from a defined excel file and written
        into a database.

        The format of the excel is documented in the docs.
        # TODO: Insert the Link to the excel-format documentation

        Args:
            session (Session): Database Session
            fpath (string): Path to the defined Excel sheet
        """

        try:
            df = self.ParticipantImport.loadAndPrepareParticipant(fpath=fpath)

            newPartics = df.to_dict("records")

        except Exception as exc:

            # TODO error handling
            raise exc

        for parti in newPartics:
            convPartiDict = self.convertImportNamesToAthleteKeys(parti)

            newAth = self.Athlete(**convPartiDict)

            self.DataInterface.addNewTableEntry(newAth)

    def convertImportNamesToAthleteKeys(self, importDict):

        # TODO: Make this as an importable constant
        mapping = {
            "Name": "name",
            "Vorname": "firstName",
            "Jahrgang": "birthYear",
            "Geschlecht": "sex",
            "Verein": "club",
            "Klasse": "classGroup",
        }

        return {mapping[key]: value for (key, value) in importDict.items()}
