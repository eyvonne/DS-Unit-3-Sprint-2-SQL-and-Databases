import sqlite3
from query import slqueryall
import pymongo

client = pymongo.MongoClient("mongodb://admin:59LHzInJr1DTduHm@cluster0-shard-00-00-qimtg.mongodb.net:27017,cluster0-shard-00-01-qimtg.mongodb.net:27017,cluster0-shard-00-02-qimtg.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

chars = slqueryall('SELECT * FROM charactercreator_character')
cols = ['sql_id', 'name', 'level', 'exp', 'hp', 'strength',
        'intelligence', 'dexterity', 'wisdom']
charDocs = []
for char in chars:
    chardict = {}
    for i, col in enumerate(cols):
        chardict[col] = char[i]
    charDocs.append(chardict)

db.test.insert_many(charDocs)
