import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US29
from geditdone.tablehelpers import TableHelpers

class ListDeceased(unittest.TestCase):

    def one_table(self):
        individuals = {
            "PERSON1": Individual(id="PERSON1", death=date(2019,10,1)),
            "PERSON2": Individual(id="PERSON2", death=date(2019,5,4)),
            "PERSON3": Individual(id="PERSON3", death=date(2019,4,3)),
        }
        families = {}
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US29.list_deceased(parser, db)
        self.assertEqual(len(pt_list), 1)

    def none_deceased(self):
        individuals = {
            "PERSON1": Individual(id="PERSON1"),
            "PERSON2": Individual(id="PERSON2"),
            "PERSON3": Individual(id="PERSON3"),
        }
        families = {}
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US29.list_deceased(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)

    def all_deceased(self):
        individuals = {
            "PERSON1": Individual(id="PERSON1", death=date(2005,10,5)),
            "PERSON2": Individual(id="PERSON2", death=date(2005,10,15)),
            "PERSON3": Individual(id="PERSON3", death=date(2006,9,5)),
        }
        families = {}
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US29.list_deceased(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 3)

    def runTest(self):
        self.one_table()
        self.none_deceased()
        self.all_deceased()