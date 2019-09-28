import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class BirthBeforeDeath(unittest.TestCase):
    """Makes sure births are before death"""
    def correct_order(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, date(1998, 2, 16), date(2015, 10, 6), None, None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(US03.birth_before_death(parser), True)

    def incorrect_order(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, date(2015, 10, 6), date(1998, 2, 16), None, None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(US03.birth_before_death(parser), False)

    def incorrect_birth_null(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, None, date(1998, 2, 16), None, None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(US03.birth_before_death(parser), False)

    def correct_death_null(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, date(1998, 2, 16), None, None, None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(US03.birth_before_death(parser), True)

    def correct_nulls(self):
        individuals = {
            "TEST1": Individual("TEST1", None, None, None, None, None, None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(US03.birth_before_death(parser), True)

    def runTest(self):
        self.correct_order()
        self.incorrect_order()
        self.incorrect_birth_null()
        self.correct_death_null()
        self.correct_nulls
