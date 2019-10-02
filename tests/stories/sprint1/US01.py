import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US01

class DatesBeforeCurrentDate(unittest.TestCase):

    def correct_individuals(self):
        individuals = {
            "TEST1": Individual("TEST1", name=None, sex=None, birth=None, death=date(2001, 11, 6), famc=None, fams=None),
            "TEST2": Individual("TEST2", name=None, sex=None, birth=date(1985, 11, 6), death=None, famc=None, fams=None),
            "TEST3": Individual("TEST3", name=None, sex=None, birth=None, death=None, famc=None, fams=None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(len(US01.dates_before_current_date(parser)), 0)

    def incorrect_individuals(self):
        individuals = {
            "TEST1": Individual("TEST1", name=None, sex=None, birth=None, death=date(2070, 11, 6), famc=None, fams=None),
            "TEST2": Individual("TEST2", name=None, sex=None, birth=date(2077, 11, 6), death=None, famc=None, fams=None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(len(US01.dates_before_current_date(parser)), 2)

    def correct_families(self):
        families = {
            "TEST1": Family("TEST1", [], None, None, date(2018, 10, 5), None),
            "TEST2": Family("TEST2", [], None, None, None, date(1994, 10, 5)),
            "TEST3": Family("TEST3", [], None, None, None, None)
        }
        parser = TestParser({}, families)
        self.assertEqual(len(US01.dates_before_current_date(parser)), 0)

    def incorrect_families(self):
        families = {
            "TEST1": Family("TEST1", [], None, None, date(2078, 10, 5), None),
            "TEST2": Family("TEST2", [], None, None, None, date(2076, 10, 5))
        }
        parser = TestParser({}, families)
        self.assertEqual(len(US01.dates_before_current_date(parser)), 2)

    def runTest(self):
        self.correct_individuals()
        self.incorrect_individuals()
        self.correct_families()
        self.incorrect_families()
