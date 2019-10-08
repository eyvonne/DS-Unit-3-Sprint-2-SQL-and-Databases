import sqlite3
import psycopg2


def pgquery(command):
    '''This function takes in a sql query against my playground database on
    elephantsql'''
    dbname = 'epgwreqv'
    user = 'epgwreqv'
    password = 'UGV3og2aGaAW2fP03tIgO9t868osOezT'
    host = 'salt.db.elephantsql.com'
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                               password=password, host=host)
    pg_curs = pg_conn.cursor()
    pg_curs.execute(command)
    try:
        result = pg_curs.fetchall()
    except:
        result = None
    pg_curs.close()
    pg_conn.commit()
    return result


def slqueryall(command):
    '''This function takes in an sql query against the local sqlite3 database'''
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    result = curs.execute(command).fetchall()
    curs.close()
    conn.commit()
    return result


def slqueryone(command):
    '''This function takes in an sql query against the local sqlite3 database'''
    conn = sqlite3.connect('rpg_db.sqlite3')
    curs = conn.cursor()
    result = curs.execute(command).fetchone()
    curs.close()
    conn.commit()
    return result
