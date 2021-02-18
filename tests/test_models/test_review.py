#!/usr/bin/python3
""" Tests for Review class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review
import models


class TestingReview(unittest.TestCase):
    """ Review class - tests """
    def test_Review1(self):
        """ Test of the Review class """
        my_Review1 = Review()

    def test_Review2(self):
        """ Test of the Review class """
        my_Review2 = Review(1)
        my_Review3 = Review("hola")
        my_Review4 = Review([1, 2, 3])
        my_Review5 = Review({"hola": "chau"})

    def test_Review3(self):
        """ Test of the Review class """
        self.assertEqual(str(type(Review)), "<class 'type'>")

    def test_Review4(self):
        """ Test of the Review class """
        my_Review6 = Review()
        self.assertEqual(isinstance(my_Review6, Review), True)

    def test_Review5(self):
        """ Test of the Review class """
        my_Review7 = Review()
        self.assertEqual(issubclass(Review, BaseModel), True)

    def test_Review6(self):
        """ Test of the Review class """
        self.assertEqual(issubclass(Review, FileStorage), False)

    def test_Review7(self):
        """ Test of the Review class """
        my_Review8 = Review()
        my_Review8.place_id = "Dortmund"
        my_Review8.user_id = "Julian"
        my_Review8.text = "Very nice"
        self.assertEqual(type(my_Review8.place_id), str)
        self.assertEqual(type(my_Review8.user_id), str)
        self.assertEqual(type(my_Review8.text), str)
        # self.assertEqual(my_Review8.id, "Dortmund")
        # self.assertEqual(my_Review8.id, "Julian")

    def test_Review8(self):
        """ Test of the Review class """
        my_Review9 = Review()
        my_Review9.place_id = "Marco"
        my_Review9.user_id = "Reus"
        my_Review9.text = "11"
        self.assertTrue("place_id" in my_Review9.__dict__)
        self.assertTrue("user_id" in my_Review9.__dict__)
        self.assertTrue("text" in my_Review9.__dict__)

    def test_Review9(self):
        """ Test of the Review class """
        my_Review10 = Review()
        self.assertFalse("first" in my_Review10.__dict__)

    def test_Review10(self):
        """ Test of the Review class """
        my_review11 = Review()
        self.assertEqual(type(my_review11.place_id), str)
        self.assertEqual(type(my_review11.user_id), str)
        self.assertEqual(type(my_review11.text), str)

    """def test_Review10N(self):
        self.assertEqual(Review, type(Review()))
        self.assertEqual(str, type(Review().id))
    def test_Review11N(self):
        my_Review11 = Review()
        my_Review12 = Review()
        self.assertNotEqual(my_Review11.id, my_Review12.id)"""

if __name__ == "__main__":
    unittest.main()
