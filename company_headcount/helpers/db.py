import sqlite3


class Db:
    """
    A class used to represent database(Db)
    """
    def __init__(self, database):
        """Connect to sqlite and create a cursor object
        Arguments:
            database(str): string of the database path
        """
        self.conn = sqlite3.connect(database)
        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

    def execute(self, query):
        """ Execute query and commit current transaction
        Arguments:
            query (str): string of query content
        """
        self.cursor.execute(query)
        self.conn.commit()

    def fetchall(self, query):
        """Retrieves all the rows in the result
         of a query and return them as a list of dictionaries
        Arguments:
            query (str): string of query content
        Returns:
            retrieved data
        """
        self.cursor.execute(query)
        self.conn.commit()
        result = [dict(row) for row in self.cursor.fetchall()]
        return result

    def close(self):
        """Close the connection
        """
        self.conn.close()
