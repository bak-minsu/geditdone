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
                print("Invalid!")
                break
    
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
