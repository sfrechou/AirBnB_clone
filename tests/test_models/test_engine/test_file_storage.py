#!/usr/bin/python3
""" Tests for FileStorage class """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import os
import sys
import pep8
import unittest


class TestingFileStorage(unittest.TestCase):
    """ FileStorage class - tests """
    def test_PreData1(self):
        """ Test of the PreData """
        with self.assertRaises(TypeError):
            PreData1 = FileStorage("Holberton")
        with self.assertRaises(TypeError):
            PreData2 = FileStorage(2)
        with self.assertRaises(TypeError):
            Predata4 = FileStorage({"hola": "chau"})
        with self.assertRaises(TypeError):
            PreData5 = FileStorage([1, 2, 3])

    def test_PreData2(self):
        """ Test of the PreData """
        PreData6 = FileStorage()
        PreData6.name = "Jadon"
        PreData6.my_number = 7
        self.assertTrue(isinstance(PreData6, FileStorage))
        self.assertTrue(type(PreData6), object)
        self.assertEqual(str(type(FileStorage)), "<class 'type'>")

    def test_new1(self):
        """ Test of the new func """
        PreData7 = FileStorage()
        PreData8 = BaseModel()
        PreData8.name = "Matt"
        PreData8.my_number = 15
        PreData7.new(PreData8)
        with self.assertRaises(AttributeError):
            (BaseModel.__objects[PreData8.__class__.__name__ +
             "." + str(PreData8.id)])

    def test_all1(self):
        """ Test of the all func """
        PreData9 = FileStorage()
        PreData9.save()
        all_objs = models.storage.all()
        self.assertIsNotNone(all_objs)

    def test_all2(self):
        """ test all """
        PreData100 = FileStorage()
        PreData1000 = PreData100.all()
        self.assertIsNotNone(PreData1000)
        self.assertEqual(type(PreData1000), dict)

    def test_pep8(self):
        """Pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_reload(self):
        """reload"""
        temp_reload = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(temp_reload.reload(), None)

if __name__ == "__main__":
    unittest.main()
