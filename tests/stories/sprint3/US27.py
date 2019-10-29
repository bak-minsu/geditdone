import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US27
from geditdone.datehelpers import DateHelpers

'''Ensure that age added to table is correct'''
class includeAges(unittest.TestCase):

    def testBirth(self):
        individuals = {
            "PERSON1": Individual(id="PERSON1", birth=date(1990,10,1))
        }
        families = {}
        parser = TestParser(individuals, families)
        # Code taken from US27
        # Need to call with set date instead of current date for testing
        result = None
        for indiv in parser.individuals.values():
            if indiv.birth is not None:
                result = DateHelpers.calculate_age(indiv.birth, date(2019, 1, 1))
            else:
                result = None
        self.assertEqual(result, 28)

    def nullBirth(self):
        individuals = {
            "PERSON1": Individual(id="PERSON1")
        }
        families = {}
        parser = TestParser(individuals, families)
        result = None
        for indiv in parser.individuals.values():
            if indiv.birth is not None:
                result = DateHelpers.calculate_age(indiv.birth, date(2019, 1, 1))
            else:
                result = None
        self.assertEqual(result, None)

    def runTest(self):
        self.testBirth()
        self.nullBirth()