import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US30
from tests.testhelpers import TestParser, TestDatabase
from geditdone.tablehelpers import TableHelpers

class ListLivingMarried(unittest.TestCase):

    def living_married(self):
        individuals = {
            "HUSB1": Individual(id="HUSB1", fams="FAM1"),
            "WIFE1": Individual(id="WIFE1", fams="FAM1"),
            "HUSB2": Individual(id="HUSB2", fams="FAM2"),
            "WIFE2": Individual(id="WIFE2", fams="FAM2"),
            "WIFE3": Individual(id="WIFE3", famc="FAM3"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=None, husband_id="HUSB1", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB2", wife_id="WIFE2"),
        }

        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US30.list_living_married(parser, db)
        #print(pt_list)
        self.assertGreater(TableHelpers.get_row_count(pt_list[0]), 0)

    def runTest(self):
        self.living_married()