#!/usr/bin/python3
"""modul containing a class for states object"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Class of states, containing names and id"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states',
                          cascade="all, delete")
