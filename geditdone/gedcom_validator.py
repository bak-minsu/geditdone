import sys
import inspect
from geditdone.gedcom_objects import GedcomError
# Try not to import unnecessary packages
from geditdone.stories import *

class Validator:
    def __init__(self, parser):
        """Initializes the class with families and individuals"""
        self.parser = parser

    # TODO: Return an error when invalid
    def validate(self):
        stories = self.get_all_stories()
        for story in stories:
            errors = story(self.parser)
            if len(errors) > 0:
                self.invalid(story, errors)
            else:
                # WARNING: Testing purposes only
                self.valid(story)

    def get_all_stories(self):
        """Gets all functions in stories folder"""
        functions = []
        modules = sys.modules.keys()

        for module in modules:
            if "geditdone.stories." in module:
                function_list = eval("inspect.getmembers({}, inspect.isfunction)".format(module[-4:]))
                functions.append(function_list[0][1])

        # print(functions)
        return functions

    def invalid(self, function, errors):
        """What to do when the validator returns invalid"""
        for error in errors:
            print(error.toString())

    # for debugging
    def valid(self, function):
        """What to do when the validator returns valid"""
        print("Function {} successfully passed!".format(function.__name__))
