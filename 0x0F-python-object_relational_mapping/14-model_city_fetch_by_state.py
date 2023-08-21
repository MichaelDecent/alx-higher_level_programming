#!/usr/bin/python3
"""
This Module Contains script that prints all City Object
from the database 'hbtn_0e_14_usa'
"""
from model_state import State, Base
from model_city import City
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    # selecting the columns to be printed out
    rows = session.query(State.name, City.id, City.name).join(City).all()
    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")

    session.close()
