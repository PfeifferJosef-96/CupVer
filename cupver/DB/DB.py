from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

Base = declarative_base()


class DataInterface(object):
    def __init__(self):

        self.session = None

    def connectToDatabase(self, session):
        """Connect the Interface to a database

        Args:
            session (sql.Session): The session to connect to
        
        Returns:
            0 -> no error
            -1 -> error occured
        """
        ret_val = 0
        try:
            # TODO check type of session
            self.session = session

        except Exception as exc:

            ret_val = -1

        return ret_val

    def disconnectFromDatabase(self, session):

        self.session = None

    def addNewTableEntry(self, tableRow):

        try:
            self.session.add(tableRow)

        except Exception as exc:
            # TODO: Split up the exception type!
            self.session.rollback()

            print("Error - Check Import")
            rowId = -1
        else:
            self.session.commit()
            rowId = tableRow.id

        finally:

            self.session.close()
            return rowId

    def convertQueryToDict(self, Query):
        """Converts the given Query to dictionary
        format
        """

        dictOut = {
            colName.name: getattr(Query, colName.name)
            for colName in Query.__table__.columns
        }

        return dictOut

    def queryWholeTable(self, tableClass):
        """Get all Information from Table.
        Each row in the is converted to dict.

        Args:
            session (Session): sqlalchemy session
        
        Returns:
            dictOut (dict): keys are integer!
                All information from the table
                in dictionary format.
        """

        queryList = self.session.query(tableClass).order_by(tableClass.id).all()

        dictOut = {}
        for it, row in enumerate(queryList):
            dictOut[it] = self.convertQueryToDict(row)

        return dictOut

    def resetWholeDatabase(self):
        pass

    def queryRowByID(self, table, id):

        query = self.session.query(Athlete).filter_by(id=1).first()

        return query
