#!/usr/bin/python3
""" Filter states by user input """

import sys
import MySQLdb

if __name__ == "__main__":
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_database = sys.argv[3]
    db_search = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=db_user, passwd=db_password,
        db=db_database
    )

    cur = db.cursor()
    select_search = "SELECT id, name FROM states\
                    WHERE name = %(db_search)s ORDER BY id ASC"
    cur.execute(select_search, {'db_search': db_search})
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
