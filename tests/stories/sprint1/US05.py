import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US05

class MarriageBeforeDeath(unittest.TestCase):
    """Makes sure mariages come before death"""

    def correctSeq(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", date(2014, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US05.marriage_before_death(parser)), 0)

    def incorrectSeqHusb(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=date(2013, 9, 4), famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", date(2014, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertGreater(len(US05.marriage_before_death(parser)), 0)

    def incorrectSeqWife(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2013, 9, 4), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", date(2014, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertGreater(len(US05.marriage_before_death(parser)), 0)

    def nullMarriage(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", None, None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US05.marriage_before_death(parser)), 0)

    def nullDeath(self):
        individuals = {
            "HUSB1": Individual("HUSB1", name=None, sex=None, birth=None, death=None, famc=None, fams="TEST1"),
            "WIFE1": Individual("WIFE1", name=None, sex=None, birth=None, death=date(2015, 11, 6), famc=None, fams="TEST1")
        }
        families = {
            "TEST1": Family("TEST1", [], "HUSB1", "WIFE1", date(2014, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US05.marriage_before_death(parser)), 0)
    
    def runTest(self):
        self.correctSeq()
        self.incorrectSeqHusb()
        self.incorrectSeqWife()
        self.nullMarriage()
        self.nullDeath()
