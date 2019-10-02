import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US06

class DivorceBeforeDeath(unittest.TestCase):
    """Makes sure divorces occur before death"""

    def incorrect_divorces(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=date(2013, 11, 6), famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", None, date(2014, 10, 5))
        }
        parser = TestParser(individuals, families)
        self.assertGreater(len(US06.divorce_before_death(parser)), 0)

    def runTest(self):
        self.incorrect_divorces()