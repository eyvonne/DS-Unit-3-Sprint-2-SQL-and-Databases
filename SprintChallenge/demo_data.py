import sqlite3


def query(query):
    '''this function takes in a SQL query and connects to
    the demo_data.sqlite3 database to execute it.
    Its on my list of things to do to wrap it up in a class
    And put it into a module on pypi so I don't have to keep
    writting it again and again for different databases'''
    conn = sqlite3.connect('demo_data.sqlite3')
    curs = conn.cursor()
    result = curs.execute(query).fetchall()
    curs.close()
    conn.commit()
    conn.close()
    return result


# create the table
create_table = '''CREATE TABLE demo (
                s VARCHAR(1),
                x INT,
                y INT
                );'''
query(create_table)

# insert the data
insertion = '''INSERT INTO demo (s, x, y)
            VALUES ('g', 3,9),('v', 5,7),('f', 8, 7);'''
query(insertion)

# How many rows are there
print('number of rows')
print(query('SELECT count(*) FROM demo;'))

# How many rows with x and y both >= 5
print('number of rows with x and y greater than 5')
print(query('''SELECT COUNT(*) FROM demo
                WHERE x>=5 AND y>=5;'''))

# how many unique values of y are there
print('number of unique y values')
print(query('''SELECT COUNT(DISTINCT y) FROM demo;'''))
