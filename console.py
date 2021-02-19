#!/usr/bin/python3
""" Console for the airbnb program """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ class of console commands """
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City",
               "Amenity", "Place", "Review"]

    def do_EOF(self, args):
        """ Exit the program """
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """ Nothing going on """
        pass

    def do_create(self, args):
        """ Creates instances of class """
        if not args:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(args)()
            print(new.id)
            new.save()

    def do_show(self, args):
        """ Str representation of instances """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
        else:
            new_obj = storage.all()
            print("[{}] ({}) {}".format(i[0], i[1], new_obj[key_search]))

    def do_destroy(self, args):
        """ Deletes instances based on ID """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
        else:
            new_obj = storage.all()
            del new_obj[key_search]
            with open("file.json", mode='r') as my_file:
                json_data = json.load(my_file)
                del json_data[key_search]
            with open("file.json", mode='w') as my_f:
                my_f.write(json.dumps(json_data))

    def do_all(self, args):
        """ Prints all the str representation of the instances """
        list_obj = []
        new_obj = storage.all()
        if args and args not in self.classes:
            print("** class doesn't exist **")
            return
        if args in self.classes:
            for key, value in new_obj.items():
                if args in key:
                    split_key = key.split(".")
                    new_key = "[" + split_key[0] + "] (" + split_key[1] + ")"

                    list_obj.append(new_key + " " + str(value))
        else:
            for key, value in new_obj.items():
                list_obj.append(str(key) + " " + str(value))
        print(list_obj)

    def do_update(self, args):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute
        """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
            return
        if len(i) == 2:
            print("** attribute name missing **")
            return
        if len(i) == 3:
            print("** value missing **")
            return
        for key, value in storage.all().items():
            if key == key_search:
                for key2 in value.keys():
                    if key2 == i[2]:
                        value[key2] = i[3].strip('"')
                        return
                value[i[2]] = i[3].strip('"')
                return

    def do_count(self, args):
        """ Prints amount of instances of a class """
        count = 0
        if args in self.classes:
            instances = storage.all()
            for key in instances.keys():
                class_n = key.split(".")
                if class_n[0] == args:
                    count += 1
        print(count)

    def default(self, args):
        """ Default """
        functs = {'all': 'do_all', 'show': 'do_show', 'update': 'do_update',
                  'destroy': 'do_destroy', 'count': 'do_count'}
        splits = args.split(".")
        class_name = splits[0]
        class_name.capitalize()
        if class_name in self.classes:
            rest = splits[1]
            diction = False
            if any("{" in elem for elem in rest):
                        diction = True
            remove = ['(', ')', ',', '"', '{', '}', ':', "'"]
            for i in remove:
                rest = rest.replace(i, ' ')
            elements = rest.split()
            if len(elements) == 1:
                for key, value in functs.items():
                    if key == elements[0]:
                        funct = 'self.' + value + '("' + class_name + '")'
                        eval(funct)
            elif len(elements) == 2:
                for key, value in functs.items():
                    if key == elements[0]:
                        funct = 'self.' + value + '("' + class_name + ' '\
                                + elements[1] + '")'
                        eval(funct)
            elif len(elements) >= 3:
                # if len(elements) == 3:
                    attrs = elements[2:]
                    att = 0
                    val = 1
                    s = 'self.'
                    e = ' '
                    for key, value in functs.items():
                        if key == elements[0]:
                            for elems in range(len(attrs)):
                                if diction is False:
                                    funct = s + value + '("' + class_name + e\
                                            + elements[1] + e + attrs[att]\
                                            + e + attrs[val] + '")'
                                    eval(funct)
                                    break
                                else:
                                    funct = s + value + '("' + class_name\
                                            + e + elements[1] + e + attrs[att]\
                                            + e + attrs[val] + '")'
                                    eval(funct)
                                    if att + 2 < len(attrs):
                                        att += 2
                                    else:
                                        break
                                    if val + 2 < len(attrs):
                                        val += 2

        else:
            print("*** Unknown syntax: {}".format(args))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
