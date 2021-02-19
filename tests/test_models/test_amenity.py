#!/usr/bin/python3
""" Tests for Amenity class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
import models
import pep8


class TestingAmenity(unittest.TestCase):
    """ Amenity class - tests """
    def test_User1(self):
        """ Test of the Amenity class """
        my_amenity1 = User()

    def test_Amenity2(self):
        """ Test of the Amenity class """
        my_amenity2 = Amenity(1)
        my_amenity3 = Amenity("hola")
        my_amenity4 = Amenity([1, 2, 3])
        my_amenity5 = Amenity({"hola": "chau"})

    def test_Amenity3(self):
        """ Test of the Amenity class """
        self.assertEqual(type(Amenity), type)

    def test_Amenity4(self):
        """ Test of the Amenity class """
        my_amenity6 = Amenity()
        self.assertEqual(isinstance(my_amenity6, Amenity), True)

    def test_Amenity5(self):
        """ Test of the Amenity class """
        my_amenity7 = Amenity()
        self.assertEqual(issubclass(Amenity, BaseModel), True)

    def test_Amenity6(self):
        """ Test of the Amenity class """
        self.assertEqual(issubclass(Amenity, FileStorage), False)

    def test_Amenity7(self):
        """ Test of the Amenity class """
        my_amenity8 = Amenity()
        my_amenity8.name = "Andy"
        self.assertEqual(type(my_amenity8.name), str)

    def test_Amenity8(self):
        """ Test of the Amenity class """
        my_amenity9 = Amenity()
        my_amenity9.name = "Gini"
        self.assertTrue("name" in my_amenity9.__dict__)

    def test_Amenity8_2(self):
        """ Test of the Amenity class """
        my_amenity92 = Amenity()
        my_amenity92.name = "Trent"
        self.assertTrue(type(my_amenity92.name), str)

    def test_Amenity9(self):
        """ Test of the Amenity class """
        my_amenity10 = Amenity()
        self.assertFalse("first" in my_amenity10.__dict__)

    def test_Amenity10(self):
        """ Test of the Amenity class """
        my_amenity11 = Amenity()
        self.assertEqual(type(my_amenity11.id), str)

    def test_Amenity11(self):
        """ Test of the city class """
        my_amenity12 = Amenity()
        my_amenity13 = Amenity()
        self.assertNotEqual(my_amenity12.id, my_amenity13.id)

    def test_Amenity12(self):
        """ Test of the city class """
        self.assertEqual(Amenity, type(Amenity()))
        self.assertEqual(str, type(Amenity().id))

    def test_Amenity13(self):
        """pep8 test amenity"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_Amenity14(self):
        """Tests amenity"""
        s = "[Amenity] ({}) {}"
        my_amenity14 = Amenity()
        my_amenity14printed = my_amenity14.__str__()
        self.assertEqual(my_amenity14printed,
                         s.format(my_amenity14.id, my_amenity14.__dict__))

    def test_hasattribute(self):
        """Tests amenity"""
        my_amenity15 = Amenity()
        self.assertTrue(hasattr(my_amenity15, "__init__"))
        self.assertTrue(hasattr(my_amenity15, "created_at"))
        self.assertTrue(hasattr(my_amenity15, "updated_at"))
        self.assertTrue(hasattr(my_amenity15, "id"))

if __name__ == "__main__":
    unittest.main()
