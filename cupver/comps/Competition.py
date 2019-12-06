class Competition(object):
    def __init__(self, ParticipantImport, Athlete, Location):

        self.ParticipantImport = ParticipantImport()
        self.Athlete = Athlete
        self.Location = Location

    def connectToDatabase(self, fpath, newDatabase=True):

        self.CompDatabase.setDatabaseConnection(fpath, newDatabase)

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

            for parti in newPartics:
                convPartiDict = self.convertImportNamesToAthleteKeys(parti)

                newAth = self.Athlete(**convPartiDict)
                session.add(newAth)

        except Exception as exc:
            # TODO: Split up the exception type!
            session.rollback()

            print("Error - Check Import")

        else:
            session.commit()

        finally:
            session.close()

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
