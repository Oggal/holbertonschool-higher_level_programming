#!/usr/bin/python3
"""Fetch All States"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def insert_into_states():
    '''Fetch All States'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()
    print("{}".format(state.id))


if __name__ == "__main__":
    insert_into_states()
