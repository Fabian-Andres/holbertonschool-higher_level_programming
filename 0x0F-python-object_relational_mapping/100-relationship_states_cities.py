#!/usr/bin/python3
""" Cities in state """
import sys
from relationship_state import Base, State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = 'California'
    session.add(new_state)
    session.commit()

    new_city = City()
    new_city.name = 'San Francisco'
    new_city.state_id = new_state.id
    session.add(new_city)
    session.commit()
