import pytest
from sqlalchemy import create_engine

from cupver.DB.DB import Base, DataInterface, Session
from cupver.DB.Tables.Athlete import Athlete


@pytest.fixture(scope="module")
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

