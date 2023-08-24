#!/usr/bin/python3
"""
This Module contains a script that creates
a table 'City' in database 'hbtn_0e_14_usa'
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base


class City(Base):
    """
    This class defines a table 'cities' which inherites from the base table
    """
    __tablename__ = 'cities'
    id = Column(
        Integer, unique=True, primary_key=True,
        nullable=False, autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
