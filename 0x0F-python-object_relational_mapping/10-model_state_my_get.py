#!/usr/bin/python3
"""
This Module contains a script that lists all
State objects that contains 'a' from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    db = argv[3]
    state_name = argv[4]

    # create and connects with the datatbase
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == {state_name}).first()
    if state:
        print(state.id)
    elif state is not state_name:
        print("Not found")

    session.close()
