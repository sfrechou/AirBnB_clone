#!/usr/bin/python3
""" Tests for BaseModel class """


import unittest
import datetime
from models.base_model import BaseModel


class TestingBaseModel(unittest.TestCase):
    """ BaseModel class - tests """
    def test_PreData1(self):
        """ Test of the PreData """
        PreData1 = BaseModel("Holberton")
        PreData2 = BaseModel(2)
        PreData3 = BaseModel()
        Predata4 = BaseModel({"hola": "chau"})
        PreData5 = BaseModel([1, 2, 3])

    def test_PreData2(self):
        """ Test of the PreData """
        PreData6 = BaseModel()
        PreData6.name = "Holberton"
        PreData6.my_number = 7
        self.assertTrue(isinstance(PreData6, BaseModel))
        self.assertTrue(type(PreData6), object)
        self.assertEqual(str(type(BaseModel)), "<class 'type'>")

    def test_Save1(self):
        """ Test of the Save func """
        PreData7 = BaseModel()
        PreData7.name = "Virgil"
        PreData7.my_number = 4
        PreData7.save()
        self.assertNotEqual(PreData7.created_at, PreData7.updated_at)

    def test_Save2(self):
        """ Test of the Save func """
        PreData8 = BaseModel()
        PreData8.name = "Erling"
        PreData8.my_number = 9
        old_date = PreData8.created_at
        PreData8.save()
        self.assertEqual(old_date, PreData8.created_at)

    def test_to_Dict1(self):
        """ Test of the to_dict func """
        PreData9 = BaseModel()
        PreData9.name = "Mohammed"
        PreData9.my_number = 11
        self.assertEqual(PreData9.to_dict()["id"], PreData9.id)
        self.assertEqual(PreData9.to_dict()["my_number"], PreData9.my_number)
        self.assertEqual(PreData9.to_dict()["name"], PreData9.name)
        self.assertEqual(PreData9.to_dict()["__class__"], "BaseModel")
        self.assertEqual(PreData9.to_dict()["created_at"],
                         PreData9.created_at.isoformat())
        self.assertEqual(PreData9.to_dict()["updated_at"],
                         PreData9.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
