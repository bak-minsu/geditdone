import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US02

class BirthBeforeMarriage(unittest.TestCase):
    """Makes sure births are before marriage"""
    def births_before_marriage(self):
        """Checks both people in the marriage were born before the marriage"""
        pass