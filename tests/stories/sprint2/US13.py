import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US13

class SiblingSpacing(unittest.TestCase):

    def siblings_greater_than_9_months(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2013, 4, 14), death=None, famc="FAM", fams=None),
            "CHILD2": Individual("CHILD2", name=None, sex=None, birth=None, death=None, famc="FAM", fams=None),
            "CHILD3": Individual("CHILD3", name=None, sex=None, birth=date(2014, 6, 7), death=None, famc="FAM", fams=None)
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD1","CHILD2","CHILD3"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US13.sibling_spacing(parser)), 0)

    def siblings_less_than_9_months(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2013, 4, 14), death=None, famc="FAM", fams=None),
            "CHILD2": Individual("CHILD2", name=None, sex=None, birth=date(2015, 1, 12), death=None, famc="FAM", fams=None),
            "CHILD3": Individual("CHILD3", name=None, sex=None, birth=date(2014, 6, 7), death=None, famc="FAM", fams=None)
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD1","CHILD2","CHILD3"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US13.sibling_spacing(parser)), 1)

    def no_siblings(self):
        individuals = {
            "DAD": Individual("DAD", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "MOM": Individual("MOM", name=None, sex=None, birth=None, death=None, famc=None, fams="FAM"),
            "CHILD1": Individual("CHILD1", name=None, sex=None, birth=date(2013, 4, 14), death=None, famc="FAM", fams=None)
        }
        families = {
            "FAM": Family("FAM", child_ids=["CHILD1"], husband_id="DAD", wife_id="MOM", married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US13.sibling_spacing(parser)), 0)

    def runTest(self):
        self.siblings_greater_than_9_months()
        self.siblings_less_than_9_months()
        self.no_siblings()
