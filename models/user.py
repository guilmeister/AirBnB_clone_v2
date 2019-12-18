#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    """
    __tablename__ = 'users'
    id = Column(String(128), primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """
    places = relationship("Place", cascade="all, delete-orphan")
    reviews = relationship("Review", cascade="all, delete-orphan")
    """
