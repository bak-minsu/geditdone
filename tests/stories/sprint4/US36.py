import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US36
from geditdone.tablehelpers import TableHelpers

class ListRecentDeaths(unittest.TestCase):

    def Recent(self):
        individuals = {
            "RECENT": Individual(id="RECENT", death=date(2000,1,15)),
            "OLD": Individual(id="OLD", death=date(1989,7,31))
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US36.list_recent_deaths(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 1)

    def noneRecent(self):
        individuals = {
            "OLD1": Individual(id="OLD1", death=date(1990,2,22)),
            "OLD2": Individual(id="OLD2", death=date(1991,6,16))
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US36.list_recent_deaths(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)

    def nullDeath(self):
        individuals = {
            "NULLBIRT": Individual(id="NULLBIRT", death=None)
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US36.list_recent_deaths(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)

    def runTest(self):
        # self.recent()
        # self.noneRecent()
        # self.nullDeath()
        pass