#!/usr/bin/python3
""" List all state objects from the database """
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    ses = Session(engine)
    state_a = ses.query(State).filter_by(name=argv[4]).first()
    if state_a:
        print("{}".format(state_a.id))
    else:
        print("Not found")
    ses.close()
