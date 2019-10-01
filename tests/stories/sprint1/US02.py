import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US02

class BirthBeforeMarriage(unittest.TestCase):

    def no_children(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", [], None, None, date(2054, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US02.birth_before_marriage(parser)), 0)

    def child_no_birth_date(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "SON": Individual("SON", name=None, sex=None, birth=None, death=None, famc="FAM", fams=None),
        }
        families = {
            "FAM": Family("FAM", ["SON"], None, None, date(2054, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US02.birth_before_marriage(parser)), 0)

    def child_birth_after_marriage(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "SON": Individual("SON", name=None, sex=None, birth=date(2011, 6, 6), death=None, famc="FAM", fams=None),
        }
        families = {
            "FAM": Family("FAM", ["SON"], None, None, date(2010, 9, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US02.birth_before_marriage(parser)), 0)

    def child_birth_at_marriage(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "SON": Individual("SON", name=None, sex=None, birth=date(2010, 11, 6), death=None, famc="FAM", fams=None),
        }
        families = {
            "FAM": Family("FAM", ["SON"], None, None, date(2010, 11, 6), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US02.birth_before_marriage(parser)), 1)

    def child_birth_before_marriage(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "SON": Individual("SON", name=None, sex=None, birth=date(2010, 11, 6), death=None, famc="FAM", fams=None),
        }
        families = {
            "FAM": Family("FAM", ["SON"], None, None, date(2012, 10, 5), None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US02.birth_before_marriage(parser)), 1)

    def runTest(self):
        self.no_children()
        self.child_no_birth_date()
        self.child_birth_after_marriage()
        self.child_birth_at_marriage()
        self.child_birth_before_marriage()