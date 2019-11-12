import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US35
from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers

class ListRecentBirths(unittest.TestCase):

    def recent(self):
        individuals = {
            "RECENT": Individual(id="RECENT", birth=date.today()),
            "OLD": Individual(id="OLD", birth=date(1989,7,31))
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US35.list_recent_births(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 1)

    def noneRecent(self):
        individuals = {
            "OLD1": Individual(id="OLD1", birth=date(1990,2,22)),
            "OLD2": Individual(id="OLD2", birth=date(1991,6,16))
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US35.list_recent_births(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)

    def nullBirth(self):
        individuals = {
            "NULLBIRT": Individual(id="NULLBIRT", birth=None)
        }

        parser = TestParser(individuals, {})
        db = TestDatabase(individuals, {})
        pt_list = US35.list_recent_births(parser, db)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 0)

    def runTest(self):
        self.recent()
        self.noneRecent()
        self.nullBirth()