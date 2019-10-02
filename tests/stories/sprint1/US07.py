import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US07

class LessThan150YearsOld(unittest.TestCase):
    """Makes sure nobody reaches 150 years old"""
    def incorrect_age(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, date(1800, 2, 16), date(2015, 10, 6), None, None)
        }
        parser = TestParser(individuals, {})
        self.assertGreater(len(US07.less_than_150_years_old(parser)), 0)

    def runTest(self):
        self.incorrect_age()