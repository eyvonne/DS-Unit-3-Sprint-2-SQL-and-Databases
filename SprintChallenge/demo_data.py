from query import SqlQueries
import sqlite3

cursor = SqlQueries('demo_data.sqlite3')


def createTable():
    '''creates the table'''
    create_table = '''CREATE TABLE demo (
                    s VARCHAR(1),
                    x INT,
                    y INT
                    );'''
    cursor.cquery(create_table)


def insertData():
    '''inserts the data given'''
    print('Put the data into the table')
    insertion = '''INSERT INTO demo (s, x, y)
                VALUES ('g', 3,9),('v', 5,7),('f', 8, 7);'''
    cursor.cquery(insertion, table='demo')


def countRows():
    '''prints number of rows, output: 3'''
    print('number of rows')
    cursor.tquery('SELECT count(*) FROM demo;')


def xYgreaterthan5():
    '''prints number of rows where x and y are both >=5, output: 2'''
    print('number of rows with x and y greater than 5')
    cursor.tquery('''SELECT COUNT(*) FROM demo
                    WHERE x>=5 AND y>=5;''')


def uniqueY():
    '''prints count of unique y values, output: 2'''
    print('number of unique y values')
    cursor.tquery('''SELECT COUNT(DISTINCT y) FROM demo;''')
