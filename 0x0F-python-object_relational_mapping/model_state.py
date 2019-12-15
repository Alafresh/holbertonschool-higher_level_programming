#!/usr/bin/python3
""" First State Model """
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Information about tables"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
