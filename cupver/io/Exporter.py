import pandas as pd
from openpyxl import load_workbook

from cupver.NameConvert import OnTimeNames


class OnTimeExporter(object):
    """Export Athletes to OnTime readable
    Excel Format.
    """

    def __init__(self):

        self.dataFrameColumns = [
            OnTimeNames.START_NO,
            OnTimeNames.NAME,
            OnTimeNames.FIRST_NAME,
            OnTimeNames.SEX,
            OnTimeNames.BIRTH_YEAR,
            OnTimeNames.CLUB,
            OnTimeNames.INFO,
            OnTimeNames.NATION,
            OnTimeNames.CLASS_GROUP,
        ]

        self.dtypeColumns = [int, str, str, str, int, str, str, str, str]

        self.columnFormatDict = {
            OnTimeNames.START_NO: self.startNoColConverter,
            OnTimeNames.NAME: self.nameColConverter,
            OnTimeNames.FIRST_NAME: self.nameColConverter,
            OnTimeNames.SEX: self.sexColConverter,
            OnTimeNames.BIRTH_YEAR: self.birthYearColConverter,
            OnTimeNames.CLUB: self.clubColConverter,
            OnTimeNames.INFO: self.classGroupColConverter,
            OnTimeNames.NATION: self.nationGroupColConverter,
            OnTimeNames.CLASS_GROUP: self.classGroupColConverter,
        }

    def exportDataFrameToFile(self, data, path):
        """Export the participant data to an excel file.

        Args:
            data (dict): Dict with the participant data.
            path (pathlib.Path): Full path to output file


        Example for data:
            #TODO


        Returns:
            statusCode (int): Code specifying if everything passed
                or an error occured.
        """
        preparedDataFrame = self.setUpDataframe(data)
        writer = self.prepareTemplate(path)
        
        preparedDataFrame.to_excel(writer,sheet_name='Starterliste', index=False, header=False, startrow=1)

        writer.save()


    def prepareTemplate(self, path):
        
        book = load_workbook('./templates/OnTime10_Anmeldung.xlsm', keep_vba=True)
        
        writer = pd.ExcelWriter(path, engine='openpyxl', model='a') 
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

        return writer



    def setUpDataframe(self, data):

        prepData = self.prepareColumnsOfData(data)

        dataFrame = pd.DataFrame.from_dict(
            data=data, orient="index", columns=self.dataFrameColumns
        )

        return dataFrame

    def prepareColumnsOfData(self, data):
        """Rename the dictionary keys to the needed format
        and apply converter functions to the values. This
        makes sure that all columns have the excpected OnTime
        Format.
        """

        for key in data.keys():
            data[key] = {
                OnTimeNames().convertFromInternal(subkey): value
                for subkey, value in data[key].items()
            }

            data[key] = {
                subkey : self.columnFormatDict[subkey](value) for subkey, value in data[key].items()
            }

        return data

    @staticmethod
    def startNoColConverter(x):

        if type(x) is not int:
            x = 9999

        if 0 < x <= 9999:
            retVal = x

        else:
            retVal = 9999

        return retVal

    @staticmethod
    def nameColConverter(x):

        retVal = x
        if type(x) is not str:
            retVal = "N/A"

        retVal = retVal[:35]

        return retVal

    @staticmethod
    def sexColConverter(x):

        maleSyn = ["M", "m", "männlich", "Männlich"]
        femaleSyn = ["W", "w", "weiblich", "Weiblich"]

        retVal = x

        if type(retVal) is not str:
            retVal = "X"

        if retVal in maleSyn:
            retVal = "M"

        elif retVal in femaleSyn:
            retVal = "W"

        else:
            retVal = "X"

        return retVal

    @staticmethod
    def birthYearColConverter(x):

        if type(x) is not int:
            retVal = 1900
            
        else:
            retVal = x

        return x

    @staticmethod
    def clubColConverter(x):
        
        if type(x) is not str:
            x = str(x)
        
        return x

    @staticmethod
    def classGroupColConverter(x):

        if type(x) is not str:
            x = str(x)

        x = x[:50]

        return x 

    @staticmethod
    def nationGroupColConverter(x):
        return x
