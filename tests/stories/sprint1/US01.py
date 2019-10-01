import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US01

class DatesBeforeCurrentDate(unittest.TestCase):

    def individual_dates_after_today(self):
        individuals = {
            "TEST1": Individual("TEST1", name=None, sex=None, birth=None, death=date(2030, 11, 6), famc=None, fams="TEST1"),
            "TEST2": Individual("TEST2", name=None, sex=None, birth=date(2035, 11, 6), death=None, famc=None, fams="TEST1")
        }
        parser = TestParser(individuals, {})
        self.assertGreater(len(US01.dates_before_current_date(parser)), 0)

    def family_dates_after_today(self):
        families = {
            "TEST1": Family("TEST1", [], None, None, date(2044, 10, 5), None),
            "TEST2": Family("TEST2", [], None, None, None, date(2054, 10, 5))
        }
        parser = TestParser({}, families)
        self.assertGreater(len(US01.dates_before_current_date(parser)), 0)
        pass

    def runTest(self):
        pass
