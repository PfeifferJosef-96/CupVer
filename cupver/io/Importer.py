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

            convCols.append(OnTimeNames().convertToInternalFromResult(colName))

        df.columns = convCols

        return df

    def importResultFile(self, path, returnFormat="records"):
        """Import an OnTime Result file into an
        dataframe

        Args:
            path (pathlib.Path): Full path to result file
            returnFormat (str): --> records: dataframe.to_dict('records')
                                --> df: dataframe
        Returns:
            df (pd.Dataframe / dict): Dataframe with the content of the
                result file and converted for internal usage.
                Format depends on "returnFormat"


        """

        rawDf = self.readDataframe(path)
        df = self.convertDataframeColumns(rawDf)

        if returnFormat == "records":
            retVal = df.to_dict("records")
        elif returnFormat == "df":

            retVal = df

        else:
            
            raise KeyError

        return retVal

