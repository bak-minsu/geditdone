import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class MarriageBeforeDivorce(unittest.TestCase):

    def correct_sequence(self):
        families = {
            "TEST1": Family("TEST1", None, None, None, married=date(2015, 10, 5), divorced=date(2015, 10, 6)),
        }
        parser = TestParser({}, families)
        self.assertEqual(US04.marriage_before_divorce(parser), True)

    def incorrect_sequence(self):
        families = {
            "TEST1": Family("TEST1", None, None, None, married=date(2015, 10, 6), divorced=date(2015, 10, 5)),
        }
        parser = TestParser({}, families)
        self.assertEqual(US04.marriage_before_divorce(parser), False)
    
    def correct_null_dates(self):
        families = {
            "TEST1": Family("TEST1", None, None, None, married=None, divorced=None),
            "TEST1": Family("TEST1", None, None, None, married=date(2015, 10, 6), divorced=None),
        }
        parser = TestParser({}, families)
        self.assertEqual(US04.marriage_before_divorce(parser), True)

    def incorrect_null_dates(self):
        families = {
            "TEST1": Family("TEST1", None, None, None, married=None, divorced=date(2015, 10, 6)),
        }
        parser = TestParser({}, families)
        self.assertEqual(US04.marriage_before_divorce(parser), False)

    def runTest(self):
        self.correct_sequence()
        self.incorrect_sequence()
        self.correct_null_dates()
        self.incorrect_null_dates()