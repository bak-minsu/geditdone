import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US02

class BirthBeforeMarriage(unittest.TestCase):
    """Makes sure births are after marriage"""
    def birth_before_marriage(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "SON": Individual("SON", name=None, sex=None, birth=date(2010, 11, 6), death=None, famc="FAM", fams=None),
        }
        families = {
            "FAM": Family("FAM", ["SON"], None, None, date(2054, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertGreater(len(US02.birth_before_marriage(parser)), 0)

    def runTest(self):
        self.birth_before_marriage()