import unittest
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US39
from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

class UpcomingAnniversaries(unittest.TestCase):

    def setUp(self):
        self.today = date.today()

    def one_table(self):
        marriage = date(2001, self.today.month, self.today.day)
        individuals = {}
        families = {
            "FAM1": Family(id="FAM1", married=DateHelpers.add_time(marriage, 15, "day")),
            "FAM2": Family(id="FAM2", married=DateHelpers.add_time(marriage, 16, "day")),
            "FAM3": Family(id="FAM3", married=DateHelpers.add_time(marriage, 1, "day")),
        }
        parser = TestParser(individuals, families)
        pt_list = US39.upcoming_anniversaries(parser)
        self.assertEqual(len(pt_list), 1)
    
    def no_table(self):
        marriage = date(2001, self.today.month, self.today.day)
        individuals = {}
        families = {
            "FAM1": Family(id="FAM1", married=DateHelpers.add_time(marriage, 35, "day")),
            "FAM2": Family(id="FAM2", married=DateHelpers.add_time(marriage, 36, "day")),
            "FAM3": Family(id="FAM3", married=DateHelpers.add_time(marriage, 100, "day")),
        }
        parser = TestParser(individuals, families)
        pt_list = US39.upcoming_anniversaries(parser)
        self.assertEqual(len(pt_list), 0)

    def one_anniversary(self):
        marriage = date(2001, self.today.month, self.today.day)
        individuals = {}
        families = {
            "FAM1": Family(id="FAM1", married=DateHelpers.add_time(marriage, 15, "day")),
            "FAM2": Family(id="FAM2", married=DateHelpers.add_time(marriage, 36, "day")),
            "FAM3": Family(id="FAM3", married=DateHelpers.add_time(marriage, 100, "day")),
        }
        parser = TestParser(individuals, families)
        pt_list = US39.upcoming_anniversaries(parser)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 1)

    def two_anniversaries(self):
        marriage = date(2001, self.today.month, self.today.day)
        individuals = {}
        families = {
            "FAM1": Family(id="FAM1", married=DateHelpers.add_time(marriage, 15, "day")),
            "FAM2": Family(id="FAM2", married=DateHelpers.add_time(marriage, 16, "day")),
            "FAM3": Family(id="FAM3", married=DateHelpers.add_time(marriage, 100, "day")),
        }
        parser = TestParser(individuals, families)
        pt_list = US39.upcoming_anniversaries(parser)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 2)

    def runTest(self):
        self.one_table()
        self.no_table()
        self.one_anniversary()
        self.two_anniversaries()