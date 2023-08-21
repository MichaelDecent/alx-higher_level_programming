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

    # create and connects with the datatbase
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    update_user = session.query(State).filter(State.id == 2).first()
    update_user.name = 'New Mexico'

    session.add(update_user)
    session.commit()

    session.close()
