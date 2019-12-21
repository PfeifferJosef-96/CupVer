from pathlib import Path

import mock
import pandas as pd
import pytest

from cupver.io.Importer import OnTimeImporter
from cupver.NameConvert import InternalNames, OnTimeNames

lenMockDataframe = 1000


def newReadDataframe(*args):

    cols = [OnTimeNames.RES_INFO, OnTimeNames.RES_RANK]

    resInfo = [it for it in range(0, lenMockDataframe)]
    resRank = [it for it in range(lenMockDataframe, 0, -1)]

    data = dict(zip(cols, [resInfo, resRank]))

    df = pd.DataFrame(data=data, columns=cols)

    return df


@pytest.fixture
def Importer():

    with mock.patch.object(OnTimeImporter, "readDataframe", newReadDataframe):

        yield OnTimeImporter()


def test_newReadDataframe(Importer):

    df = OnTimeImporter.readDataframe()

    assert all([OnTimeNames.RES_INFO, OnTimeNames.RES_RANK] == df.columns)
    assert len(df[OnTimeNames.RES_INFO]) == lenMockDataframe
    assert df[OnTimeNames.RES_INFO][0] == 0
    assert df[OnTimeNames.RES_RANK][0] == lenMockDataframe


@pytest.mark.skip()
def test_readDataframe():

    pass


@pytest.mark.parametrize("test_data", [("df"), ("records"), ("something")])
def test_importResultFile(Importer, test_data):

    path2File = Path("someValidPath")

    expecColNames = [InternalNames.ID, InternalNames.RES_RANK]

    if test_data == "records":

        retDf = Importer.importResultFile(path2File, test_data)
        assert all([it in expecColNames for it in retDf[0].keys()])
        assert type(retDf) is list
        assert type(retDf[0]) is dict

    elif test_data == "df":

        retDf = Importer.importResultFile(path2File, test_data)
        assert all(expecColNames == retDf.columns)
        assert type(retDf) is pd.DataFrame

    else:
        with pytest.raises(KeyError):

            retDf = Importer.importResultFile(path2File, test_data)
