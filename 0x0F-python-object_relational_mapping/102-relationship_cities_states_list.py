#!/usr/bin/python3
"""lists all City objects from the database
uses the state relationship to access to the
State object linked to the City object
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city in session.query(City).order_by(City.id).all():
        print("{0}: {1} -> {2}".format(city.id, city.name, city.states.name))
