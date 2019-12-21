class InternalNames(object):
    """Names of columns that are used in the
    database and other internal usage"""

    NAME = "name"
    FIRST_NAME = "firstName"
    CLASS_GROUP = "classGroup"
    BIRTH_YEAR = "birthYear"
    SEX = "sex"
    CLUB = "club"
    ID = "id"

    RES_RANK = "rank"


class OnTimeNames(object):
    """Names that are used by the OnTime time
    recording software."""

    # Names of the "Meldungen" table
    START_NO = "Startnr"
    NAME = "Nachname"
    FIRST_NAME = "Vorname"
    SEX = "Geschlecht"
    BIRTH_YEAR = "Geburtsjahr"
    CLUB = "Mannschaft"
    INFO = "Zusatzinfo"
    NATION = "Nation"
    CLASS_GROUP = "Klasse"

    # Names of a "Ergebnis" - table
    RES_START_NO = "StNr"
    RES_NAME_FIRSTNAME = "Name"  # Name and First Name in same cell
    RES_BIRTH_YEAR = "JG"
    RES_SEX = "Sex"
    RES_CLUB = "Vereinsname"
    RES_INFO = "Info"
    RES_RANK = "Rang"

    def __init__(self):

        self.internalToOnTimeDict = {
            InternalNames.NAME: self.NAME,
            InternalNames.FIRST_NAME: self.FIRST_NAME,
            InternalNames.CLASS_GROUP: self.CLASS_GROUP,
            InternalNames.BIRTH_YEAR: self.BIRTH_YEAR,
            InternalNames.SEX: self.SEX,
            InternalNames.CLUB: self.CLUB,
            InternalNames.ID: self.INFO,
        }

        self.onTimeResultToInternal = {
            self.RES_INFO: InternalNames.ID,
            self.RES_RANK: InternalNames.RES_RANK,
        }

    def convertFromInternal(self, name):
        """Convert an internal name of an attribute
        to an OnTime Name. If the requested Name
        is not availiable, "N/A" is returned.

        Args:
            name (str): Internal  Name of Attribute

        Returns:
            convName (str): On Time Name

        """
        try:
            convName = self.internalToOnTimeDict[name]

        except KeyError as keyErr:
            convName = "N/A"

        return convName

    def convertToInternalFromResult(self, name):
        """Convert Names from OnTime Result File
        """
        try:
            convName = self.onTimeResultToInternal[name]

        except KeyError as keyErr:
            convName = "N/A"

        return convName

