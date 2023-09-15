#!/usr/bin/python3
"""script that lists all states entered by user from the
database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    """connect to database and execute query"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY \
            '{}' ORDER BY id ASC"
        .format(args[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
