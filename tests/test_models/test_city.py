#!/usr/bin/python3
""" Tests for City class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.city import City
import models
import pep8


class TestingCity(unittest.TestCase):
    """ City class - tests """
    def test_City1(self):
        """ Test of the City class """
        my_City1 = City()

    def test_City2(self):
        """ Test of the City class """
        my_City2 = City(1)
        my_City3 = City("hola")
        my_City4 = City([1, 2, 3])
        my_City5 = City({"hola": "chau"})

    def test_City3(self):
        """ Test of the City class """
        self.assertEqual(type(City), type)

    def test_City4(self):
        """ Test of the City class """
        my_City6 = City()
        self.assertEqual(isinstance(my_City6, City), True)

    def test_City5(self):
        """ Test of the City class """
        my_City7 = City()
        self.assertEqual(issubclass(City, BaseModel), True)

    def test_City6(self):
        """ Test of the City class """
        self.assertEqual(issubclass(City, FileStorage), False)

    def test_City7(self):
        """ Test of the City class """
        my_City8 = City()
        my_City8.name = "Denver"
        self.assertEqual(type(my_City8.state_id), str)
        self.assertEqual(type(my_City8.name), str)

    def test_City8(self):
        """ Test of the City class """
        my_City9 = City()
        my_City9.state_id = "Borussia"
        my_City9.name = "Dortmund"
        self.assertTrue("state_id" in my_City9.__dict__)
        self.assertTrue("name" in my_City9.__dict__)

    def test_City9(self):
        """ Test of the City class """
        my_City10 = City()
        self.assertFalse("first" in my_City10.__dict__)

    def test_City11N(self):
        self.assertEqual(City, type(City()))
        self.assertEqual(str, type(City().id))

    def test_City12N(self):
        my_city11 = City()
        my_city12 = City()
        self.assertNotEqual(my_city11.id, my_city12.id)

    def test_pep8(self):
        """pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_City13N(self):
        """kwargs"""
        my_city13 = City(name="Denver")
        self.assertEqual(type(my_city13).__name__, "City")
        self.assertTrue(hasattr(my_city13, "name"))
        self.assertFalse(hasattr(my_city13, "id"))
        self.assertFalse(hasattr(my_city13, "created_at"))
        self.assertFalse(hasattr(my_city13, "updated_at"))
        self.assertTrue(hasattr(my_city13, "__class__"))

    def test_City14N(self):
        """str"""
        s = "[City] ({}) {}"
        my_city14 = City()
        my_city14printed = my_city14.__str__()
        self.assertEqual(my_city14printed,
                         s.format(my_city14.id, my_city14.__dict__))

    def test_City15N(self):
        """Tests """
        my_city15 = City()
        self.assertTrue(hasattr(my_city15, "__init__"))
        self.assertTrue(hasattr(my_city15, "created_at"))
        self.assertTrue(hasattr(my_city15, "updated_at"))
        self.assertTrue(hasattr(my_city15, "id"))

if __name__ == "__main__":
    unittest.main()
