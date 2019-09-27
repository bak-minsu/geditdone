import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class DivorceBeforeDeath(unittest.TestCase):
    """Makes sure divorces occur before death"""
    def runTest(self):
        pass