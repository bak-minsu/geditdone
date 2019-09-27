import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class LessThan150YearsOld(unittest.TestCase):
    """Makes sure nobody reaches 150 years old"""
    def runTest(self):
        pass