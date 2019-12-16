#!/usr/bin/python3
""" List all state objects from the database """
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    ses = Session(engine)
    new_table = ses.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for i, j in new_table:
        print('{}: ({}) {}'.format(j.name,
                                   i.id,
                                   i.name))
    ses.close()
