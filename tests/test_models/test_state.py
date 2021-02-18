#!/usr/bin/python3
""" Tests for State class """
import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
import models


class TestingState(unittest.TestCase):
    """ State State - tests """
    def test_State1(self):
        """ Test of the State class """
        my_state1 = State()

    def test_State2(self):
        """ Test of the State class """
        my_State2 = State(1)
        my_State3 = State("hola")
        my_State4 = State([1, 2, 3])
        my_State5 = State({"hola": "chau"})

    def test_State3(self):
        """ Test of the State class """
        self.assertEqual(str(type(State)), "<class 'type'>")

    def test_State4(self):
        """ Test of the State class """
        my_State6 = State()
        self.assertEqual(isinstance(my_State6, State), True)

    def test_State5(self):
        """ Test of the State class """
        my_State7 = State()
        self.assertEqual(issubclass(State, BaseModel), True)

    def test_State6(self):
        """ Test of the State class """
        self.assertEqual(issubclass(State, FileStorage), False)

    def test_State7(self):
        """ Test of the State class """
        my_State8 = State()
        my_State8.name = "Marco"
        self.assertEqual(type(my_State8.name), str)

    def test_State8(self):
        """ Test of the State class """
        my_State9 = State()
        my_State9.name = "Marco"
        self.assertTrue("name" in my_State9.__dict__)

    def test_State9(self):
        """ Test of the State class """
        my_State10 = State()
        self.assertFalse("first" in my_State10.__dict__)

    def test_State10(self):
        my_state11 = State()
        my_state12 = State()
        self.assertNotEqual(my_state11.id, my_state12.id)

    """def test_State10N(self):
        self.assertEqual(State, type(State()))
        self.assertEqual(str, type(State().id))"""

if __name__ == "__main__":
    unittest.main()
