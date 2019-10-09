import pandas as pd
from query import pgquery, slqueryall, slqueryone
import sqlite3

# these two lines of code only need to be run once to always work.
#sl_conn = sqlite3.connect('rpg_db.sqlite3')
#pd.read_csv('titanic.csv').to_sql('Titanic', sl_conn, index_label='id')

records = slqueryall('SELECT * FROM titanic')

create_titanic_table = '''
    CREATE TABLE titanic(
    id SERIAL PRIMARY KEY,
    survived INT,
    pclass INT,
    name TEXT,
    sex TEXT,
    age INT,
    siblingsSpouses INT,
    parentsChildren INT,
    fare REAL)'''
pgquery(create_titanic_table)

for r in records:
    if "'" in r[3]:
        insertion = '''INSERT INTO titanic
                (survived, pclass, name, sex, age, siblingsSpouses, parentsChildren, fare)
                VALUES ('''+str(r[1])+', '+str(r[2])+', \''+r[3].replace("'", "''")+'\', \''+str(r[4])+'\', '+str(r[5])+', '+str(r[6])+', '+str(r[7])+', '+str(r[8])+');'
        print(insertion)
    else:
        insertion = '''INSERT INTO titanic
                    (survived, pclass, name, sex, age, siblingsSpouses, parentsChildren, fare)
                    VALUES'''+str(r[1:])+';'
    pgquery(insertion)
