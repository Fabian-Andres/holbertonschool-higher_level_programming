#!/usr/bin/python3
""" All cities by state """

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) == 5:
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
        cur.execute("SELECT c.name FROM cities AS c\
                    JOIN states AS s ON c.state_id = s.id\
                    WHERE s.name LIKE BINARY '{:s}'\
                    ORDER BY c.id ASC".format(db_search))
        rows = cur.fetchall()

        list_states = []
        for row in rows:
            list_states.append(row[0])

        print(", ".join(list_states))

        cur.close()
        db.close()
