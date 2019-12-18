#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), nullable=False, ForeignKey('places.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    """

    place_id = ""
    user_id = ""
    text = ""

    """
    user = relationship("User", backref=backref("Review",
                                                cascade="all, delete-orphan"))
    place = relationship("Place", backref=backref("Review",
                                                  cascade="all, delete-orphan"))
    """
