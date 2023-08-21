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
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.ilike("%a%")).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
