#!/usr/bin/python3
""" state model module """
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

argv = sys.argv
Base = declarative_base()


class State(Base):
    """State Class to represent states"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement="auto", nullable=False)
    name = Column(String(128), nullable=False)
