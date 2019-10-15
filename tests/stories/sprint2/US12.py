import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US12

class ParentsNotTooOld(unittest.TestCase):

    def correct(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1945, 10, 6), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1985, 10, 6), death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 0)

    def incorrectMom(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1945, 10, 6), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1945, 10, 6), death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 1)

    def incorrectDad(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1900, 10, 6), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1985, 10, 6), death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 1)

    def nullBirth(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1945, 10, 6), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1985, 10, 6), death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 0)

    def nullMomBirth(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=date(1945, 10, 6), death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 0)

    def nullDadBirth(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=date(1985, 10, 6), death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US12.parents_not_too_old(parser)), 0)

    def runTest(self):
        self.correct()
        self.incorrectMom()
        self.incorrectDad()
        self.nullBirth()
        self.nullMomBirth()
        self.nullDadBirth()