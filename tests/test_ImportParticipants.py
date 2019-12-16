import pytest

import pandas as pd


@pytest.fixture
def classDf():
    """Dataframe which defines classes in import file.
    """

    columns = ["columns1", "columns2"]
    df = pd.DataFrame()

    return df
