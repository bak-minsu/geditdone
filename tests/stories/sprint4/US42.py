import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US42
from geditdone.error_objects import GedcomError, ErrorType

class RejectIllegitimateDates(unittest.TestCase):

    def correct_individuals(self):
        individuals = {
            "TEST1": Individual("TEST1", name="Person1", sex=None, birth="2021-2-28", death="2007-8-31", famc=None, fams=None),
            "TEST2": Individual("TEST2", name="Person2", sex=None, birth="2020-2-29", death="1944-7-31", famc=None, fams=None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(len(US42.reject_illegitimate_dates(parser)), 0)

    def incorrect_individuals(self):
        individuals = {
            "TEST3": Individual("TEST3", name="Person3", sex=None, birth="2021-2-29", death="2007-8-32", famc=None, fams=None),
            "TEST4": Individual("TEST4", name="Person4", sex=None, birth="1976-11-31", death="-1874-9-30", famc=None, fams=None)
        }
        parser = TestParser(individuals, {})
        self.assertEqual(len(US42.reject_illegitimate_dates(parser)), 4)

    def correct_families(self):
        families = {
            "TEST5": Family("TEST5", child_ids=[], husband_id=None, wife_id=None, married="1900-10-5", divorced="2002-1-31"),
            "TEST6": Family("TEST6", child_ids=[], husband_id=None, wife_id=None, married="1849-3-31", divorced="2011-4-30"),
        }
        parser = TestParser({}, families)
        self.assertEqual(len(US42.reject_illegitimate_dates(parser)), 0)

    def incorrect_families(self):
        families = {
            "TEST7": Family("TEST7", child_ids=[], husband_id=None, wife_id=None, married="1963-13-5", divorced="2016-1-32"),
            "TEST8": Family("TEST8", child_ids=[], husband_id=None, wife_id=None, married="2018-0-31", divorced="2018-2-30"),
        }
        parser = TestParser({}, families)
        self.assertEqual(len(US42.reject_illegitimate_dates(parser)), 4)

    def runTest(self):
        self.correct_individuals()
        self.incorrect_individuals()
        self.correct_families()
        self.incorrect_families()