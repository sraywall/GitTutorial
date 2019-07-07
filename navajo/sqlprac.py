#!/usr/bin/python3
import sqlite3

db = sqlite3.connect("mydb")

cursor = db.cursor()
cursor.execute("DROP TABLE english")
db.commit()
f = open("English.csv")
rows = f.readlines()
columns = rows[0].split()
cursor.execute("""
       CREATE TABLE english({} INTEGER PRIMARY KEY, {} TEXT,
                        {} TEXT, {} TEXT , {} TEXT) 
        """.format(columns[0],
            columns[1],
            columns[2],
            columns[3],
            columns[4]))
for row in rows[1:]:
    r = row.split("\t")
    cursor.execute("""INSERT INTO english({}, {}, {}, {}, {})
            VALUES(?,?,?,?,?)""".format(
            columns[0],
            columns[1],
            columns[2],
            columns[3],
            columns[4]),
            (int(r[0]),r[1],r[2],r[3],r[4])
            )

    db.commit()

db.commit()
