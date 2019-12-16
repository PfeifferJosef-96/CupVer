import pandas as pd
import pytest

from cupver.io.Exporter import OnTimeExporter
from cupver.NameConvert import OnTimeNames


@pytest.fixture
def Exporter():

    return OnTimeExporter()


def test_prepareDataFrame(Exporter):
    pass


def test_prepareColumnsOfData(Exporter):
    pass


@pytest.mark.parametrize(
    "test_input, expected", [("string", 9999), (1, 1), (100000, 9999)]
)
def test_startNoColConverter(Exporter, test_input, expected):

    retVal = Exporter.startNoColConverter(test_input)

    assert retVal == expected


@pytest.mark.parametrize(
    "test_input, expected", [("string", "string"), (1, "N/A"), ("a" * 100, "a" * 35)]
)
def test_nameColConverter(Exporter, test_input, expected):

    retVal = Exporter.nameColConverter(test_input)

    assert retVal == expected
    assert len(retVal) <= 35


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("M", "M"),
        ("m", "M"),
        ("w", "W"),
        ("weiblich", "W"),
        ("männlich", "M"),
        ("Männlich", "M"),
        ("Weiblich", "W"),
        (2324, "X"),
        ("asdfa", "X"),
    ],
)
def test_sexColConverter(Exporter, test_input, expected):

    retVal = Exporter.sexColConverter(test_input)

    assert retVal == expected


def test_setUpDataframe(Exporter):

    columns = [
        "Startnr",
        "Nachname",
        "Vorname",
        "Geschlecht",
        "Geburtsjahr",
        "Mannschaft",
        "Zusatzinfo",
        "Nation",
        "Klasse",
    ]
    excptDataframe = pd.DataFrame()

    gotDataframe = Exporter.setUpDataframe()

    assert excptDataframe == gotDataframe
