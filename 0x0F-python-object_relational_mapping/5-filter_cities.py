#!/usr/bin/python3
"""lists cities of a given state state"""
import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    """connect to database and execute query"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT name FROM cities WHERE state_id = \
            (SELECT id FROM states WHERE name LIKE BINARY %s)", (args[4],))
    query = cur.fetchone()
    states = []
    while query:
        for item in query:
            states.append(item)
        query = cur.fetchone()
    print(", ".join(states))
    cur.close()
    db.close()
