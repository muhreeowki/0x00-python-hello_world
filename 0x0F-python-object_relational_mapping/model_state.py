#!/usr/bin/python3
""" state model module """
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

argv = sys.argv
Base = declarative_base()
engine = sqlalchemy.create_engine(
    "mysql://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])
)


class state(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement="auto", nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
