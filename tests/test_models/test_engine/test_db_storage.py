#!/usr/bin/python3

"""
DataBase Storage
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import unittest
import pep8


class TestDBStorage(unittest.TestCase):
    """
    DataBase testing
    """

    def testUser(self):
        """
        test user
        """
        result = User(name="NotEdward")
        self.assertTrue(user.name, "NotEdward")

    def testState(self):
        """
        test state
        """
        result = State(name="Wakanda")
        self.assertTrue(state.name, "Wakanda")

    def testCity(self):
        """
        test city
        """
        result = City(name="Manila")
        self.assertTrue(city.name, "Manila")

    def testAmenity(self):
        """
        test amenity
        """
        result = Amenity(name="nuts")
        self.assertTrue(amenity.name, "nuts")

    def testPlace(self):
        """
        test place
        """
        result = Place(name="Rocker")
        self.assertTrue(place.name, "Rocker")

    def testReview(self):
        """
        test review
        """
        result = Review(text="ayaya")
        self.assertTrue(review.text, "ayaya")

    def test_pep8_FileStorage(self):
        """
        Tests pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
