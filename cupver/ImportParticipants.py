import pathlib

import pandas as pd


class ImportParticipants(object):
    """Import the participants from the participant consolidation
    file. This is an excel file, which contains a sheet named "Meldungen"
    with the information about participants and the sheet "Klassen" which
    defines the participant classes.

    Args:

    """

    MELDUNG_SHEET_NAME = "Meldungsliste"
    KLASSEN_SHEET_NAME = "Klassen"

    def __init__(self):

        self.neededParticipantColumns = [
            "Name",
            "Vorname",
            "Jahrgang",
            "Geschlecht",
            "Verein",
        ]
        self.neededClassConfColumns = [
            "Klasse",
            "Geschlecht",
            "jüngstJahrg",
            "ältestJahrg",
        ]

    def loadAndPrepareParticipant(self, fpath):
        """Load the neede sheets from the xlsx sheets and prepare
        a dataframe, that contains all information about the
        participant.

        Args:
            fpath (str): Path to a excel file containing all information
                about participants and classes

        Returns:
            prepDf (pd.Dataframe): A dataframe containing all needed
            information about the participant
        """

        partDf = self.importParticipantSheet(fpath)
        classDf = self.importClassDefSheet(fpath)

        prepDf = self.assignClassToParticipant(partDf=partDf, classDf=classDf)

        return prepDf

    def assignClassToParticipant(self, partDf: pd.DataFrame, classDf: pd.DataFrame):

        partDf["Klasse"] = ""  # Init new column with an empty string

        for index, row in partDf.iterrows():
            # TODO: Get the correct class for Participant, not birthyear
            birthYear = partDf.get_value(index, "Jahrgang")
            partiClass = self.getClassNameOfParticipant(
                partDf.get_value(index, "Geschlecht"), birthYear, classDf
            )
            partDf.set_value(index, "Klasse", partiClass)

        return partDf.copy()

    def getClassNameOfParticipant(
        self, sex: str, birthYear: int, classDf: pd.DataFrame
    ):
        """Get a class name based on the participants birthYear and sex.
        """

        for dat in classDf.itertuples():
            
            # TODO: The named tuple is dangerous because of changing column names!!!
            lowLim = dat.jüngstJahrg <= birthYear >= dat.ältestJahrg
            sexAtt = dat.Geschlecht == sex

            if lowLim and sexAtt:
                return dat.Klasse

    def importParticipantSheet(self, fpath: pathlib.Path):
        """Import the sheet out of the definition file, that contains the
        participants.
            Args:

        """
        return self.importSheet(
            fpath, self.MELDUNG_SHEET_NAME, self.neededParticipantColumns
        )

    def importClassDefSheet(self, fpath: pathlib.Path):
        """Import the sheet out of the definition file containing the
        class definition.
            Args:

        """
        return self.importSheet(
            fpath, self.KLASSEN_SHEET_NAME, self.neededClassConfColumns
        )

    def importSheet(self, fpath: pathlib.Path, sheetName: str, columns: list):

        df = pd.read_excel(fpath, sheet_name=sheetName, columns=columns)

        return df
