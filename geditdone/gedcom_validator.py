import sys
import inspect
from geditdone.stories import *
from geditdone.gedcom_db import GedcomDatabase

class Validator:
    def __init__(self, parser):
        """Initializes the class with families and individuals"""
        self.parser = parser

    def validate(self):
        stories = self.get_all_stories()
        for story in stories:
            story(self.parser)

    def get_all_stories(self):
        """Gets all functions in stories folder"""
        functions = []
        modules = sys.modules.keys()

        for module in modules:
            if "geditdone.stories." in module:
                # Gets a list of functions from the module, [-4:] is to get the last 4 characters, "US01" for example.
                function_list = eval("inspect.getmembers({}, inspect.isfunction)".format(module[-4:]))
                # List of tuples representing functions, where the second item is the reference to the function
                functions.append(function_list[0][1])

        # print(functions)
        return functions
