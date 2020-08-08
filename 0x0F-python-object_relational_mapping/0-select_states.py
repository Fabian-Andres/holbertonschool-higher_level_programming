#!/usr/bin/python3
import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()

cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()

for row in rows:
    for col in row:
        if type(col) == int:
            print("(%s, " % (col), end='')
        else:
            print("'%s')" % (col), end='')
    print()
