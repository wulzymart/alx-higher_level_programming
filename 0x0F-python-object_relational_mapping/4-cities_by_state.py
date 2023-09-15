#!/usr/bin/python3
"""lists cities and state"""
import MySQLdb
from sys import argv as args

if __name__ == "__main__":
    """connect to database and execute query"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities JOIN states \
            WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
