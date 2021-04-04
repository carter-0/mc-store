import sqlite3 as sql

def getProductById():
    con = sql.connect("database/jobs.db")