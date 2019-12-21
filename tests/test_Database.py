import pytest
from sqlalchemy import create_engine

from cupver.DB.DB import Base, DataInterface, Session
from cupver.DB.Tables.Athlete import Athlete
from cupver.DB.Tables.Result import Result


@pytest.fixture
def engine():

    engine = create_engine("sqlite:///:memory:", echo=False)

    return engine


@pytest.fixture
def DataBaseInterface():

    return DataInterface()


@pytest.fixture
def session(engine):
    Session.configure(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    return session


@pytest.mark.parametrize(
    "test_input,expection",
    [
        ("invalidRow", -1),
        (Athlete(**dict(name="name", firstName="firstname", classGroup="classGroup", birthYear="birthYear", sex="sex", club="club")),
      0)],
)
def test_addNewTableEntry(DataBaseInterface, session, test_input, expection):

    DataBaseInterface.connectToDatabase(session)

    returnedID = DataBaseInterface.addNewTableEntry(test_input)

    assert returnedID == expection


def test_connectToDatabase(DataBaseInterface, session):

    # No session in function arguments

    with pytest.raises(TypeError) as typexc:
        DataBaseInterface.connectToDatabase()

    retVal = DataBaseInterface.connectToDatabase(session)

    assert retVal == 0


def test_convertQueryToDict(DataBaseInterface, session):

    DataBaseInterface.connectToDatabase(session)

    returnedDict = DataBaseInterface.convertQueryToDict()

    assert returnedDict == excpectedDict


def test_queryWholeTable(DataBaseInterface, session):

    DataBaseInterface.connectToDatabase(session)

    DataBaseInterface.queryWholeTable(Athlete)

