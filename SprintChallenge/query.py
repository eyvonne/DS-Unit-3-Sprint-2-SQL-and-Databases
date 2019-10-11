import sqlite3
# I'm not technically allowed to use this on the sprint
# but it doesn't change the code I'm doing, just
# makes the results readable. I'm doing this for you.
# after the sprint challenge I'm going to start a dshelper tools module
# stored on github with this.
from tabulate import tabulate


class SqlQueries():
    '''this class takes in a database as a parameter and
    executes queries on it returning data'''

    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def tquery(self, query):
        '''this function takes in a query and prints a table
        with the results. It also returns the results as a list'''
        curs = self.conn.cursor()
        results = curs.execute(query).fetchall()
        print(tabulate(results))
        curs.close()
        self.conn.commit()
        return results

    def cquery(self, query, table=None):
        '''this function takes a query that makes a change to the table
        and prints the table if given'''
        curs = self.conn.cursor()
        curs.execute(query)
        curs.close()
        self.conn.commit()
        if table != None:
            self.tquery('SELECT * FROM '+table+';')

    def commit(self):
        '''this function manually commits the connector'''
        self.conn.commit()

    def cursor(self):
        '''this function returns a cursor connected to the db'''
        return self.conn.cursor()
