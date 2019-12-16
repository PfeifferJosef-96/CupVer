from cupver.DB.DB import DataInterface


class Competition(object):
    def __init__(self, ParticipantImport, Athlete, CompetitionData):

        self.ParticipantImport = ParticipantImport()
        self.Athlete = Athlete
        self.CompetitionData = CompetitionData
        self.DataInterface = DataInterface()

    def getPartResult(self):
        raise NotImplementedError

    def getFinalResult(self):
        raise NotImplementedError

    def connectToDatabase(self, newSession):

        self.DataInterface.connectToDatabase(newSession)

    def addNewCompetition(self, data):
        """
        """

        cData = data["compData"]
        newComp = self.CompetitionData(**cData)
        compId = self.DataInterface.addNewTableEntry(newComp)

        resData = data["resultData"]
        resDataDict = resData.to_dict("records")

        # TODO: Write the results into the database

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
