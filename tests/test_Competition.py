import pytest
from cupver.comps.Competition import Competition
from cupver.DB.Tables.Athlete import Athlete
from cupver.DB.Tables.CompetitionData import CompetitionData
from cupver.ImportParticipants import ImportParticipants


@pytest.fixture(scope="module")
def BaseCompetition():

    return Competition(
        Athlete=Athlete,
        ParticipantImport=ImportParticipants,
        CompetitionData=CompetitionData,
    )


def test_convertImportNamesToAthleteKeys(BaseCompetition: Competition):

    oldDict = {
        "Name": "testLastName",
        "Vorname": "testFirstName",
        "Jahrgang": "testBirthYear",
        "Geschlecht": "testSex",
        "Verein": "testClub",
        "Klasse": "testclassGroup",
    }

    trueDict = {
        "name": "testLastName",
        "firstName": "testFirstName",
        "birthYear": "testBirthYear",
        "sex": "testSex",
        "club": "testClub",
        "classGroup": "testclassGroup",
    }

    convDict = BaseCompetition.convertImportNamesToAthleteKeys(oldDict)

    assert convDict["name"] == trueDict["name"]
    assert convDict["firstName"] == trueDict["firstName"]
    assert convDict["birthYear"] == trueDict["birthYear"]
    assert convDict["sex"] == trueDict["sex"]
    assert convDict["club"] == trueDict["club"]
    assert convDict["classGroup"] == trueDict["classGroup"]

