import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US09

class BirthBeforeParentDeath(unittest.TestCase):

    def correct(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2017, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=date(2018, 10, 6), famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 0)

    def incorrectMom(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2010, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=date(2018, 10, 6), famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 1)

    def incorrectDad(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2010, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=date(2018, 10, 6), famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 1)

    def nullBirth(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2017, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=date(2018, 10, 6), famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 1)

    def nullMomDeath(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2017, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 0)

    def nullDadDeath(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=date(2017, 10, 6), famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD": Individual("CHILD", name=None, sex=None, birth=date(2015, 10, 6), death=None, famc=None, fams="FAM")
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US09.birth_before_parent_death(parser)), 0)

    def runTest(self):
        # self.correct()
        # self.incorrectMom()
        # self.incorrectDad()
        # self.nullBirth()
        # self.nullMomDeath()
        # self.nullDadDeath()
