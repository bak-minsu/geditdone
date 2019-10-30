import sys
import inspect
from geditdone.error_objects import GedcomError
from geditdone.gedcom_db import GedcomDatabase
from geditdone.stories import *
from geditdone.tablehelpers import TableHelpers
from prettytable import PrettyTable

class Validator:
    def __init__(self, parser, db):
        """Initializes the class with families and individuals"""
        self.parser = parser
        self.db = db
        self.errors = []
        self.tables = []
        self.tables.append(TableHelpers.dataframe2table(self.db.individuals, "Individuals"))
        self.tables.append(TableHelpers.dataframe2table(self.db.families, "Families"))

    def get_argument_count(self, function):
        """Gets the total number of arguments in a function"""
        return len(inspect.getargspec(function)[0])

    def validate(self):
        stories = self.get_all_stories()
        for story in stories:
            # print(story.__name__)
            argument_count = self.get_argument_count(story)
            if argument_count == 1:
                self.process_return_value(story(self.parser))
            elif argument_count == 2:
                self.process_return_value(story(self.parser, self.db))

    def process_return_value(self, return_values):
        for value in return_values:
            if isinstance(value, GedcomError):
                self.errors.append(value)
            elif isinstance(value, PrettyTable):
                self.tables.append(value)


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

    def print_errors(self):
        for error in self.errors:
            print(error)

    def print_tables(self):
        for table in self.tables:
            if (hasattr(table, "title")):
                print(table.title)
            print(table)