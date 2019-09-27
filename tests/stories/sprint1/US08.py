import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class BirthBeforeParentMarriage(unittest.TestCase):
    """Makes sure birth happens after parent marriage"""
    def runTest(self):
        pass