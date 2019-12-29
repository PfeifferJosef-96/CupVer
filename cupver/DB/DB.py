from sqlalchemy import exc, text, update
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

    def addNewTableEntry(self, tableRow, commitEntry=True):
        """
        """

        try:
            self.session.add(tableRow)

            if commitEntry:
                self.session.commit()
            rowId = tableRow.getId()

        except exc.IntegrityError as irexc:
            rowId = -1
            print("Already existing entry!")
            self.session.rollback()

        except Exception as exce:
            # TODO: Split up the exception type!
            self.session.rollback()

            print("Error - Check Import")
            rowId = -1

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

        queryList = self.session.query(tableClass).all()

        dictOut = {}
        for it, row in enumerate(queryList):
            dictOut[it] = self.convertQueryToDict(row)

        return dictOut

    def resetWholeDatabase(self):
        pass

    def queryRowByID(self, table, id):

        query = self.session.query(Athlete).filter_by(id=1).first()

        return query

    def updateResultAssoc(self, athId, compId, resultId):
        """Update the result field of the ResultAssociation table
        between an existing athlete - competition mapping.

        Args:
            athId (int): Id of the athlete corresponding to resultId
            comopId (int): Id of the competition
            resultId (int): Id of the result in the database
        """
        from cupver.DB.Tables.Athlete import (
            ResultAssociation,
        )  # import here until correct import is possible

        try:

            ResultAssoc = text("resultAssociation")
            self.session.query(ResultAssociation).filter(
                ResultAssociation.athleteId == athId
            ).filter(ResultAssociation.competitionNr == compId).update(
                {"result": resultId}
            )

            self.session.commit()

        except Exception as exc:
            self.session.rollback()

            raise exc
