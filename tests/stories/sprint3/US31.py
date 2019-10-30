import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US31
from tests.testhelpers import TestParser, TestDatabase
from geditdone.tablehelpers import TableHelpers

class ListLivingSingle(unittest.TestCase):

    def living_single(self):
        individuals = {
            "HUSB": Individual(id="HUSB", birth=date(1900, 2, 11), famc="FAM1"),
            "WIFE": Individual(id="WIFE", birth=date(1930, 4, 18), famc="FAM2"),
            "HUSB2": Individual(id="HUSB2", birth=date(2000, 8, 17),  fams="FAM2"),
            "WIFE2": Individual(id="WIFE2", birth=date(1990, 9, 26), fams="FAM2"),
        }
        families = {
             "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB2", wife_id="WIFE2")
        }

        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US31.list_living_single(parser, db)
        #print(pt_list)
        self.assertGreater(TableHelpers.get_row_count(pt_list[0]), 0)

    def runTest(self):
        self.living_single()