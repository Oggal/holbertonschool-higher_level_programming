#!/usr/bin/python3
"""Fetch All States"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def fetch_all_states():
    '''Fetch All States'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    target = sys.argv[4]
    target = target.split('"')[0]
    target = target.split("'")[0]

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(
        State.name == (target)).first()
    if(state is None):
        print("Not Found")
        return
    print("{}".format(state.id))


if __name__ == "__main__":
    fetch_all_states()
