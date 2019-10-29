import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US30
from tests.testhelpers import TestParser, TestDatabase

class ListLivingMarried(unittest.TestCase):

    def living_married(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM"),
            "WIFE": Individual(id="WIFE", fams="FAM"),
        }
        families = {
            "FAM1": Family(id="FAM", married=date(2012,11,12), divorced=None, husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }

        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US30.list_living_married(parser, db)
        self.assertGreater(TableHelpers.get_row_count(pt_list[0]), 0)


    def runTest(self):
        self.living_married()