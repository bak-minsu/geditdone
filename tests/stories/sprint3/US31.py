import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US31
from tests.testhelpers import TestParser, TestDatabase

class ListLivingSingle(unittest.TestCase):

    def living_single(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM1"),
            "WIFE": Individual(id="WIFE", fams="FAM2"),
        }
        families = {}

        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US31.list_living_single(parser, db)
        self.assertGreater(TableHelpers.get_row_count(pt_list[0]), 0)


    def runTest(self):
        self.living_single()