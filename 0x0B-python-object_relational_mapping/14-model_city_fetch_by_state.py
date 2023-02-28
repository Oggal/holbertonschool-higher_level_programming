#!/usr/bin/python3
"""Fetch By States"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_by_state():
    '''Fetch All States'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for cit in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(cit.state.name, cit.id, cit.name))


if __name__ == "__main__":
    fetch_by_state()
