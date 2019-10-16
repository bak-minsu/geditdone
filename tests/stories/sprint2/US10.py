import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US10

class MarriageAfter14(unittest.TestCase):

    def marriage_after_14(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1995, 11, 13), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1997, 6, 20), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=[], husband_id="DAD", wife_id="MOM", married=date(2016, 8, 15), divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US10.marriage_after_14(parser)), 0)

    def marriage_before_mother_14(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1995, 11, 13), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1997, 6, 20), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=[], husband_id="DAD", wife_id="MOM", married=date(2010, 8, 15), divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US10.marriage_after_14(parser)), 1)

    def marriage_before_father_14(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1997, 11, 13), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1995, 6, 20), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=[], husband_id="DAD", wife_id="MOM", married=date(2010, 8, 15), divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US10.marriage_after_14(parser)), 1)

    def marriage_before_both_14(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1995, 11, 13), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1997, 6, 20), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=[], husband_id="DAD", wife_id="MOM", married=date(2008, 8, 15), divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US10.marriage_after_14(parser)), 2)

    def no_marriage(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1995, 11, 13), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1997, 6, 20), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=[], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US10.marriage_after_14(parser)), 0)

    def runTest(self):
        self.marriage_after_14()
        self.marriage_before_mother_14()
        self.marriage_before_father_14()
        self.marriage_before_both_14()
        self.no_marriage()