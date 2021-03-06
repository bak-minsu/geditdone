import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US21

class CorrectGenderForRole(unittest.TestCase):

    def correct_gender_for_role(self):
        individuals = {
            "HUSB": Individual(id="HUSB", name="Jim", sex="M", fams="FAM1"),
            "WIFE": Individual(id="WIFE", name="Pam", sex="F", fams="FAM2"),
            "CHILD": Individual(id="CHILD", name="Dwight", sex="M", famc="FAM1", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM", child_ids=["CHILD"], husband_id="HUSB", wife_id="WIFE")
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US21.correct_gender_for_role(parser)), 0)

    def runTest(self):
        self.correct_gender_for_role()