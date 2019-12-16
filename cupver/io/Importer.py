import pandas as pd

from cupver.NameConvert import OnTimeNames


class OnTimeImporter(object):
    def __init__(self):
        pass

    def readDataframe(self, path):
        """
        Args:
            path (pathlib.Path): Full path to result file
        """

        cols = [OnTimeNames.RES_INFO, OnTimeNames.RES_RANK]
        df = pd.read_excel(path, usecols=cols)

        return df

    def convertDataframeColumns(self, df):

        rawCols = df.columns

        convCols = []

        for colName in rawCols:

            convCols.append(OnTimeNames.convertToInternalFromResult)

        df.columns = convCols

        return df

    def importResultFile(self, path):
        """Import an OnTime Result file into an
        dataframe

        Args:
            path (pathlib.Path): Full path to result file

        Returns:
            df (pd.Dataframe): Dataframe with the content of the
                result file and converted for internal usage

        """

        rawDf = self.readDataframe(path)

        df = self.convertDataframeColumns(rawDf)

        return df

