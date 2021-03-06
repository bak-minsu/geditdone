import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US08

class BirthBeforeParentMarriage(unittest.TestCase):
    """Makes sure birth happens after parent marriage"""

    def correctSeq(self):
        individuals = {
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2015, 11, 6), death=None, famc=None, fams=None)
        }
        families = {
            "TEST1": Family("TEST1", ["CHILD1"], "TEST5", "TEST6", date(2015, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US08.birth_before_parent_marriage(parser)), 0)

    def incorrectSeq(self):
        individuals = {
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2014, 10, 5), death=None, famc=None, fams=None)
        }
        families = {
            "TEST1": Family("TEST1", ["CHILD1"], "TEST5", "TEST6", date(2015, 11, 6), None)
        }
        parser = TestParser(individuals, families)
        self.assertGreater(len(US08.birth_before_parent_marriage(parser)), 0)

    def birthNull(self):
        individuals = {
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {
            "TEST1": Family("TEST1", ["CHILD1"], "TEST5", "TEST6", date(2015, 11, 6), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US08.birth_before_parent_marriage(parser)), 0)

    def noKids(self):
        individuals = {
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2014, 10, 5), death=None, famc=None, fams=None)
        }
        families = {
            "TEST1": Family("TEST1", [], "TEST5", "TEST6", date(2015, 11, 6), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US08.birth_before_parent_marriage(parser)), 0)

    def runTest(self):
        self.correctSeq()
        self.incorrectSeq()
        self.birthNull()
        self.noKids()