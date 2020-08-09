#!/usr/bin/python3
""" Get all states """

import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=db_user, passwd=db_password,
        db=db_database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
