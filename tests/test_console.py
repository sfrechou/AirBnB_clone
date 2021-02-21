#!/usr/bin/python3
"""Test console"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from datetime import datetime
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class testing(unittest.TestCase):
    """ Test the Console """

    def test_prompt(self):
        """ Test prompt """
        with patch('sys.stdout', new=StringIO()) as salida:
            outputexpected = HBNBCommand.prompt
            self.assertEqual(outputexpected, "(hbnb) ")

    def setUp(self):
        """Set up tests."""
        storage.reload()

    def test_exit(self):
        """Test to validate quit works."""
        with patch("sys.stdout", new=StringIO()) as o:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_all_count(self):
        """ test count"""

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual("1\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("State.count()")
            self.assertEqual("1\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("City.count()")
            self.assertEqual("1\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Amenity.count()")
            self.assertEqual("1\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Place.count()")
            self.assertEqual("1\n", salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as o:
            HBNBCommand().onecmd("Review.count()")
            self.assertEqual("1\n", salida.getvalue())

    def test_quit_message(self):
        """ Test quit message """
        outputexpected = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_EOF_message(self):
        """ Test EOF message """
        outputexpected = "Exit the program"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_all(self):
        """ Test help all message """
        outputexpected = "Prints all the str representation of the instances"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_count(self):
        """ Test help count message """
        outputexpected = "Prints amount of instances of a class"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_create(self):
        """ Test help create message """
        outputexpected = "Creates instances of class"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_help(self):
        """ Test help help message """
        out1 = "List available commands with \""
        out2 = "help\" or detailed help with \"help cmd\"."
        outputexpected = out1 + out2
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_show(self):
        """ Test help show message """
        outputexpected = "Str representation of instances"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_destroy(self):
        """ Test help destroy message """
        outputexpected = "Deletes instances based on ID"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_update(self):
        """ Test help update message """
        out1 = "Updates an instance based on the class name"
        out2 = " and\n        id by adding or updating attribute"
        outputexpected = out1 + out2
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_help_message(self):
        """ Test only help message """
        out1 = "Documented commands (type help <topic>):\n="
        out2 = "=======================================\n"
        out3 = "EOF  all  count  create  destroy  help  quit  show  update"
        outputexpected = out1 + out2 + out3
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_empty_line_and_enter(self):
        """ Test empty line """
        outputexpected = ""
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("\n"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_sintax_error(self):
        """ Test sintax error """
        outputexpected = "*** Unknown syntax: asdas"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_create_BaseModel(self):
        """ Test create a BaseModel """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_User(self):
        """ Test create a User """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_amenity(self):
        """ Test create a Amenity """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_city(self):
        """ Test create a City """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_error(self):
        """ Test create a create class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_create_error_two(self):
        """ Test only create without class """
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_error(self):
        """ Test only show error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show asd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_only(self):
        """ Test only show """
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_class_only(self):
        """ Test only class show """
        outputexpected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_show_class_id_error(self):
        """ Test id error """
        outputexpected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel asdasd223"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_only(self):
        """ Test test_destroy_only"""
        outputexpected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_error(self):
        """ Test destroy class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy asd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_class_only(self):
        """ Test only show """
        outputexpected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_destroy_id_error(self):
        """ Test id error """
        outputexpected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel asda231"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_all_class(self):
        """ Test all class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("all asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_update_class(self):
        """ Test update class error """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("update asdas"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_eleven(self):
        """ Test task 11 """
        outputexpected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("all aasd"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_eleven_two(self):
        outputexpected = "*** Unknown syntax: asd.all()"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("asd.all()"))
            self.assertEqual(outputexpected, salida.getvalue().strip())

    def test_quit(self):
        """ checks if quit command is valid"""
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_do_ni_idea(self):
        """all with errors"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all()")
        msg = f.getvalue()[:-1]
        self.assertEqual(msg, "** class doesn't exist **")

    def resetStorage(self):
        """ test reset """
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_create_random(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random2(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random3(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random4(self):
        """ Test create a nidea """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_create_random5(self):
        """ xxxxxdddddd """
        outputexpected = "<class 'str'>"
        with patch("sys.stdout", new=StringIO()) as salida:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            xd = str(type(salida.getvalue().strip()))
            self.assertEqual(outputexpected, xd)

    def test_02_create_errors(self):
        """ xxxxxdddddd """
        output = "** class name missing **\n"
        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create")
            self.assertEqual(output, salida.getvalue())

        output = "** class doesn't exist **\n"
        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(output, salida.getvalue())

    def test_03_create(self):
        """ xxxxxdddddd """
        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create BaseModel")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            match = x.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create User")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            match = x.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create State")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            match = x.match(i_d)
            self.assertTrue(match is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create City")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            m = x.match(i_d)
            self.assertTrue(m is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create Amenity")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            m = x.match(i_d)
            self.assertTrue(m is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create Place")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            m = x.match(i_d)
            self.assertTrue(m is not None)

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd("create Review")
            i_d = salida.getvalue()
            ww = r'(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})'
            x = re.compile(ww)
            m = x.match(i_d)
            self.assertTrue(m is not None)

    def test_update_function(self):
        """ xxxxxdddddd """
        test1 = BaseModel()
        test1_id = test1.id
        test2 = User()
        test2_id = test2.id
        test3 = State()
        test3_id = test3.id
        test4 = City()
        test4_id = test4.id
        test5 = Amenity()
        test5_id = test5.id
        test6 = Place()
        test6_id = test6.id
        test7 = Review()
        test7_id = test7.id
        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('BaseModel.update("' + test1_id +
                                 '", {\'fn\': "facu", "age": 14, "w": 1.3})')
            self.assertTrue(hasattr(test1, 'fn'))
            self.assertTrue(hasattr(test1, 'age'))
            self.assertTrue(hasattr(test1, 'w'))
            HBNBCommand().onecmd("BaseModel.show(" + test1_id + ")")
            self.assertIn('facu', salida.getvalue())
            self.assertIn('14', salida.getvalue())
            self.assertIn('1', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('User.update("' + test2_id +
                                 '", {\'fn\': "mateo", "age": 21, "w": 18.7})')
            self.assertTrue(hasattr(test2, 'fn'))
            self.assertTrue(hasattr(test2, 'w'))
            HBNBCommand().onecmd("User.show(" + test2_id + ")")
            self.assertIn('mateo', salida.getvalue())
            self.assertIn('21', salida.getvalue())
            self.assertIn('18', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('State.update("' + test3_id +
                                 '", {\'fn\': "facu", "age": 14, "w": 1.3})')
            self.assertTrue(hasattr(test3, 'fn'))
            self.assertTrue(hasattr(test3, 'age'))
            self.assertTrue(hasattr(test3, 'w'))
            HBNBCommand().onecmd("State.show(" + test3_id + ")")
            self.assertIn('facu', salida.getvalue())
            self.assertIn('14', salida.getvalue())
            self.assertIn('1', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('City.update("' + test4_id +
                                 '", {\'fn\': "mateo", "age": 14, "w": 18.7})')
            self.assertTrue(hasattr(test4, 'fn'))
            self.assertTrue(hasattr(test4, 'w'))
            HBNBCommand().onecmd("City.show(" + test4_id + ")")
            self.assertIn('mateo', salida.getvalue())
            self.assertIn('14', salida.getvalue())
            self.assertIn('18', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('Amenity.update("' + test5_id +
                                 '", {\'fn\': "mateo", "age": 21, "w": 18.7})')
            self.assertTrue(hasattr(test5, 'fn'))
            self.assertTrue(hasattr(test5, 'w'))
            HBNBCommand().onecmd("Amenity.show(" + test5_id + ")")
            self.assertIn('mateo', salida.getvalue())
            self.assertIn('21', salida.getvalue())
            self.assertIn('18', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('Place.update("' + test6_id +
                                 '", {\'fn\': "facu", "age": 14, "w": 18.7})')
            self.assertTrue(hasattr(test6, 'fn'))
            self.assertTrue(hasattr(test6, 'w'))
            HBNBCommand().onecmd("Place.show(" + test6_id + ")")
            self.assertIn('facu', salida.getvalue())
            self.assertIn('14', salida.getvalue())
            self.assertIn('18', salida.getvalue())

        with patch("sys.stdout", new=StringIO()) as salida:
            HBNBCommand().onecmd('Review.update("' + test7_id +
                                 '", {\'fn\': "mateo", "age": 21, "w": 18.7})')
            self.assertTrue(hasattr(test7, 'fn'))
            self.assertTrue(hasattr(test7, 'w'))
            HBNBCommand().onecmd("Review.show(" + test7_id + ")")
            self.assertIn('mateo', salida.getvalue())
            self.assertIn('21', salida.getvalue())
            self.assertIn('18', salida.getvalue())
