#!/usr/bin/python3
""" Tests for Place class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
import models
import pep8


class TestingPlace(unittest.TestCase):
    """ Place class - tests """
    def test_Place1(self):
        """ Test of the Place class """
        my_place1 = Place()

    def test_Place2(self):
        """ Test of the Place class """
        my_place2 = Place(1)
        my_place3 = Place("hola")
        my_place4 = Place([1, 2, 3])
        my_place5 = Place({"hola": "chau"})

    def test_Place3(self):
        """ Test of the Place class """
        self.assertEqual(type(Place), type)

    def test_Place4(self):
        """ Test of the Place class """
        my_place6 = Place()
        self.assertEqual(isinstance(my_place6, Place), True)

    def test_Place5(self):
        """ Test of the Place class """
        my_place7 = Place()
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_Place6(self):
        """ Test of the Place class """
        self.assertEqual(issubclass(Place, FileStorage), False)

    def test_Place7(self):
        """ Test of the Place class """
        my_place8 = Place()
        my_place8.name = "Curtis"
        my_place8.description = "Jones"
        my_place8.number_rooms = 17
        my_place8.number_bathrooms = 18
        my_place8.max_guest = 13
        my_place8.price_by_night = 17
        my_place8.latitude = 53.430180
        my_place8.longitude = -2.926749
        self.assertEqual(type(my_place8.name), str)
        self.assertEqual(type(my_place8.description), str)
        self.assertEqual(type(my_place8.number_rooms), int)
        self.assertEqual(type(my_place8.number_bathrooms), int)
        self.assertEqual(type(my_place8.max_guest), int)
        self.assertEqual(type(my_place8.price_by_night), int)
        self.assertEqual(type(my_place8.latitude), float)
        self.assertEqual(type(my_place8.longitude), float)

    def test_Place8(self):
        """ Test of the Place class """
        my_place9 = Place()
        my_place9.name = "Curtis"
        my_place9.description = "Jones"
        my_place9.number_rooms = 17
        my_place9.number_bathrooms = 18
        my_place9.max_guest = 13
        my_place9.price_by_night = 17
        my_place9.latitude = 53.430180
        my_place9.longitude = -2.926749
        self.assertTrue("name" in my_place9.__dict__)
        self.assertTrue("description" in my_place9.__dict__)
        self.assertTrue("number_rooms" in my_place9.__dict__)
        self.assertTrue("number_bathrooms" in my_place9.__dict__)
        self.assertTrue("max_guest" in my_place9.__dict__)
        self.assertTrue("price_by_night" in my_place9.__dict__)
        self.assertTrue("latitude" in my_place9.__dict__)
        self.assertTrue("longitude" in my_place9.__dict__)

    def test_Place9(self):
        """ Test of the Place class """
        my_place10 = Place()
        self.assertFalse("first" in my_place10.__dict__)

    def test_Place10(self):
        """ Test for Place class """
        my_place10 = Place()
        self.assertEqual(type(my_place10.city_id), str)

    def test_Place11(self):
        """ Test of the Place class """
        my_place11 = Place()
        self.assertEqual(type(my_place11.user_id), str)

    def test_Place11(self):
        """ Test of the Place class """
        my_place12 = Place()
        self.assertEqual(type(my_place12.amenity_ids), list)

    def test_Place12(self):
        my_place11 = Place()
        my_place12 = Place()
        self.assertNotEqual(my_place11.id, my_place12.id)

    def test_Place13(self):
        self.assertEqual(Place, type(Place()))
        self.assertEqual(str, type(Place().id))

    def test_pep8(self):
        """test pep8 comes back clean"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_Place14(self):
        """Tests if the instance of BaseModel has been correctly made"""
        my_place14 = Place()
        self.assertTrue(hasattr(my_place14, "__init__"))
        self.assertTrue(hasattr(my_place14, "created_at"))
        self.assertTrue(hasattr(my_place14, "updated_at"))
        self.assertTrue(hasattr(my_place14, "id"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        my_place15 = Place(name="Denver")
        self.assertEqual(type(my_place15).__name__, "Place")
        self.assertTrue(hasattr(my_place15, "name"))
        self.assertFalse(hasattr(my_place15, "id"))
        self.assertFalse(hasattr(my_place15, "created_at"))
        self.assertFalse(hasattr(my_place15, "updated_at"))
        self.assertTrue(hasattr(my_place15, "__class__"))

if __name__ == "__main__":
    unittest.main()
