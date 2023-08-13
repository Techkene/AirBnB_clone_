#!/usr/bin/python3
""" User test classes """

from datetime import datetime
import inspect
from AirBnB_clone.models.user import User
from models.base_model import BaseModel
import pep8
import unittest


class Test_UserModel(unittest.TestCase):
    """ Test for User Class """
    def setup(self):
            self.model = User()
            self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "email"))
        self.assertTrue(hasattr(self.model, "password"))
        self.assertTrue(hasattr(self.model, "first_name"))
        self.assertTrue(hasattr(self.model, "last_name"))
        self.assertEqual(self.model.email, "")
        self.assertEqual(self.model.password, "")
        self.assertEqual(self.model.first_name, "")
        self.assertEqual(self.model.last_name, "")

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8 = pep8.StyleGuide(quiet=True)
        result = pep8.check_files(['modes/user.py'])
        self.assertEqual(result.total_errors, 0,
                             "Found code style errors and warnings.")

    def test_subclass(self):
        """test if User is a subclass"""
        self.assertTrue(issubclass(self.model.__class__, BaseModel), True)

if __name__ == "__main__":
    unittest.main()
