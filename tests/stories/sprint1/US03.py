import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class BirthBeforeDeath(unittest.TestCase):
    """Makes sure births are before death"""
    def runTest(self):
        self.correct_order()
        self.incorrect_order()
        self.correct_nulls()
        self.incorrect_nulls()