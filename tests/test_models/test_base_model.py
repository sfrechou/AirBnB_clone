#!/usr/bin/python3
""" Tests for BaseModel class """
import os
import models
import unittest
import datetime
from models.base_model import BaseModel
from time import sleep
import pep8


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

    def test_PreData3(self):
        """ Test of the PreData """
        PreData40 = BaseModel(None)
        self.assertNotIn(None, PreData40.__dict__.values())

    def test_Save1(self):
        """ Test of the Save func """
        PreData7 = BaseModel()
        PreData7.name = "Virgil"
        PreData7.my_number = 4
        PreData7.save()
        self.assertNotEqual(PreData7.created_at, PreData7.updated_at)

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

    def test_to_Dict2(self):
        """ Test of the to_dict func """
        PreData30 = BaseModel()
        self.assertTrue(dict, type(PreData30.to_dict()))

    def test_to_Dict3(self):
        PreData31 = BaseModel()
        with self.assertRaises(TypeError):
            PreData31.to_dict(None)

    def test_to_Dict4(self):
        PreData32 = BaseModel()
        self.assertNotEqual(PreData32.to_dict(), PreData32.__dict__)

    def test_to_Dict5(self):
        PreData33 = BaseModel()
        PreData33_dict = PreData33.to_dict()
        self.assertEqual(str, type(PreData33_dict["created_at"]))
        self.assertEqual(str, type(PreData33_dict["updated_at"]))

    def test_to_Dict6(self):
        dt = datetime.datetime.now()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat()
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    @classmethod
    def setUp(self):
        """ Test of the save func """
        try:
            os.rename("file.json", "puedesergio")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """ Test of the save func """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("puedesergio", "file.json")
        except IOError:
            pass

    def test_SaveN3(self):
        """ Test of the save func """
        my_base20 = BaseModel()
        sleep(0.05)
        first_updated_at = my_base20.updated_at
        my_base20.save()
        self.assertLess(first_updated_at, my_base20.updated_at)

    def test_SaveN4(self):
        """ Test of the save func """
        my_base21 = BaseModel()
        sleep(0.05)
        first_updated_at = my_base21.updated_at
        my_base21.save()
        second_updated_at = my_base21.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        my_base21.save()
        self.assertLess(second_updated_at, my_base21.updated_at)

    def test_SaveN5(self):
        """ Test of the save func """
        my_base22 = BaseModel()
        with self.assertRaises(TypeError):
            my_base22.save(None)

    def test_SaveN6(self):
        """ Test of the save func """
        my_base23 = BaseModel()
        my_base23.save()
        my_base23id = "BaseModel." + my_base23.id
        with open("file.json", "r") as f:
            self.assertIn(my_base23id, f.read())

    def test_SaveN7(self):
        """kwargs"""
        my_base24 = BaseModel(name="Denver")
        self.assertEqual(type(my_base24).__name__, "BaseModel")
        self.assertTrue(hasattr(my_base24, "name"))
        self.assertTrue(hasattr(my_base24, "__class__"))
        self.assertFalse(hasattr(my_base24, "id"))
        self.assertFalse(hasattr(my_base24, "created_at"))
        self.assertFalse(hasattr(my_base24, "updated_at"))

    def test_str_method(self):
        """str"""
        s = "[BaseModel] ({}) {}"
        my_base25 = BaseModel()
        my_base25printed = my_base25.__str__()
        self.assertEqual(my_base25printed,
                         s.format(my_base25.id, my_base25.__dict__))

if __name__ == "__main__":
    unittest.main()
