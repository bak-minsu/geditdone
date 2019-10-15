import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US16

class MaleLastNames(unittest.TestCase):

    def some_func(self):
        individuals = {
            "HUSB": Individual(id="HUSB", name="Jim Halpert", sex="M", fams="FAM1"),
            "WIFE": Individual(id="WIFE", name="Pam Halpert", sex="F", fams="FAM2"),
            "CHILD": Individual(id="CHILD", name="Michael Halpert", sex="M", famc="FAM1", fams="FAM2"),
            "CHILD2": Individual(id="CHILD2", name="Angela Halpert", sex="F", famc="FAM1", fams="FAM2")
        }
        families = {
            "FAM1": Family(id="FAM", child_ids=["CHILD","CHILD2"], husband_id="HUSB", wife_id="WIFE")
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        error_count = len(US16.male_last_name(parser, db))
        self.assertEqual(error_count, 0)
        pass

    def runTest(self):
        self.some_func()
