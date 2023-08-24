#!/usr/bin/python3
"""
a script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa
"""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    user = argv[1]
    pwd = argv[2]
    db = argv[3]

    # create and connects with the datatbase
    engine = create_engine(
<<<<<<< HEAD
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}")
=======
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}",
        pool_pre_ping=True)
>>>>>>> e8e86ff29e51ebe8ea09c0cdb334fa6d917d5573
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).join(City).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")