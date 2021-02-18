#!/usr/bin/python3
""" Tests for User class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import models


class TestingUser(unittest.TestCase):
    """ User class - tests """
    def test_User1(self):
        """ Test of the User class """
        my_user1 = User()

    def test_User2(self):
        """ Test of the User class """
        my_user2 = User(1)
        my_user3 = User("hola")
        my_user4 = User([1, 2, 3])
        my_user5 = User({"hola": "chau"})

    def test_User3(self):
        """ Test of the User class """
        self.assertEqual(str(type(User)), "<class 'type'>")

    def test_User4(self):
        """ Test of the User class """
        my_user6 = User()
        self.assertEqual(isinstance(my_user6, User), True)

    def test_User5(self):
        """ Test of the User class """
        my_user7 = User()
        self.assertEqual(issubclass(User, BaseModel), True)

    def test_User6(self):
        """ Test of the User class """
        self.assertEqual(issubclass(User, FileStorage), False)

    def test_User7(self):
        """ Test of the User class """
        my_user8 = User()
        my_user8.first_name = "Marco"
        my_user8.last_name = "Reus"
        my_user8.email = "11"
        my_user8.password = "[lis, ta]"
        self.assertEqual(type(my_user8.first_name), str)
        self.assertEqual(type(my_user8.last_name), str)
        self.assertEqual(type(my_user8.email), str)
        self.assertEqual(type(my_user8.password), str)

    def test_User8(self):
        """ Test of the User class """
        my_user9 = User()
        my_user9.first_name = "Marco"
        my_user9.last_name = "Reus"
        my_user9.email = "11"
        my_user9.password = "[lis, ta]"
        self.assertTrue("first_name" in my_user9.__dict__)
        self.assertTrue("last_name" in my_user9.__dict__)
        self.assertTrue("email" in my_user9.__dict__)
        self.assertTrue("password" in my_user9.__dict__)

    def test_User9(self):
        """ Test of the User class """
        my_user10 = User()
        self.assertFalse("first" in my_user10.__dict__)

if __name__ == "__main__":
    unittest.main()
