import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class MarriageBeforeDeath(unittest.TestCase):
    """Makes sure mariages come before death"""

    def setUp(self):
        # self.families = db.families
        pass
    
    def runTest(self):
        # for family in families:
        #     self.assertTrue(family.marriage < db.individual(family.partner1)[1].death)
        #     self.assertTrue(family.marriage < db.individual(family.partner2)[2].death)
        pass

    def tearDown(self):
        # self.families = None
        # self.individual = None
        pass