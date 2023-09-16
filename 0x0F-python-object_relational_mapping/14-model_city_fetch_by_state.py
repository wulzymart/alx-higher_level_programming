#!/usr/bin/python3
"""prints all City objects from the database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(
            City, State).join(State).order_by(City.id):
        print("{0}: ({1}) {2}".format(state.name, city.id, city.name))
