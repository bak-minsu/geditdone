import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US34
from geditdone.tablehelpers import TableHelpers

class ListLargeAgeDifferences(unittest.TestCase):

    def large_age_differences(self):
        individuals = {
            "HUSB1": Individual(id="HUSB1", birth=date(1967,9,30),fams="FAM1"),
            "WIFE1": Individual(id="WIFE1", birth=date(1989,7,31),fams="FAM1")
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2009,10,31), divorced=None, husband_id="HUSB1", wife_id="WIFE1")
        }

        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US34.list_large_age_differences(parser, db)
        #print(pt_list)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 2)

    def not_large_age_differences(self):

        individuals = {
            "HUSB2": Individual(id="HUSB2", birth=date(1990,2,22),fams="FAM2"),
            "WIFE2": Individual(id="WIFE2", birth=date(1991,6,16),fams="FAM2")
        }
        families = {
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB2", wife_id="WIFE2")
        }

        parser = TestParser(individuals, families)
        pt_list = US34.list_large_age_differences(parser)
        #print(pt_list)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)


    def runTest(self):
        self.large_age_differences()
        self.not_large_age_differences()