import pandas as pd
from query import pgquery, slqueryall, slqueryone


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
