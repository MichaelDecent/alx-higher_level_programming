#!/usr/bin/python3
"""
a script that creates the State “California”
with the City “San Francisco” from the database hbtn_0e_100_usa
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
        f"mysql+mysqldb://{user}:{pwd}@localhost/{db}")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).join(City).order_by(City.id).all()

    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")

    session.close()
