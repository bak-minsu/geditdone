import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US17

class NoMarriagesToChildren(unittest.TestCase):

    def incorrect_marriages(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM1"),
            "WIFE": Individual(id="WIFE", fams="FAM2"),
            "CHILD": Individual(id="CHILD", famc="FAM1", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM", child_ids=["CHILD"], husband_id="HUSB", wife_id="WIFE"),
            "FAM2": Family(id="FAM", husband_id="CHILD", wife_id="WIFE"),
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        self.assertGreater(len(US17.no_marriages_to_children(parser, db)), 0)

    def runTest(self):
        self.incorrect_marriages()