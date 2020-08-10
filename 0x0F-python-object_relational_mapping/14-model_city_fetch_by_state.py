#!/usr/bin/python3
""" Cities in state """
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = session.query(State, City).filter(State.id == City.state_id).all()

    for state, city in objs:
        print("%s: (%s) %s" % (state.name, city.id, city.name))
