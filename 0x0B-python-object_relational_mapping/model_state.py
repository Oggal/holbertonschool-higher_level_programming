#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
"""State Class File"""

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
