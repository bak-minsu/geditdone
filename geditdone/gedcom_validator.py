import sys
import inspect
# Try not to import unnecessary packages
from geditdone.stories import *

class Validator:
    def __init__(self, parser):
        """Initializes the class with families and individuals"""
        self.parser = parser

    # TODO: Return an error when invalid
    def validate(self):
        tests = self.get_all_functions()
        for test in tests:
            if not test(self.parser):
                self.invalid(test)
                # break
                continue # comment this and uncomment 'break'
            else:
                self.valid(test)

    def get_all_functions(self):
        """Gets all functions in stories folder"""
        functions = []
        modules = sys.modules.keys()

        for module in modules:
            if "geditdone.stories." in module:
                function_list = eval("inspect.getmembers({}, inspect.isfunction)".format(module[-4:]))
                functions.append(function_list[0][1])

        # print(functions)
        return functions

    def invalid(self, function):
        """What to do when the validator returns invalid"""
        print("Function {} is invalid!".format(function.__name__))

    # for debugging
    def valid(self, function):
        """What to do when the validator returns valid"""
        print("Function {} is valid!".format(function.__name__))
