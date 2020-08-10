#!/usr/bin/python3
""" Get a state """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State)
    .filter(State.name.like(sys.argv[4]))
    .first()

    if first_state:
        print(first_state.id)
    else:
        print("Not found")
