import unittest
import gedcom_parser
from datetime import date

class MarriageBeforeDivorce(unittest.TestCase):
    """Makes sure marriage come before a divorce"""
    def setUp(self):
        # self.families = db.families

    def runTest(self):
        """Makes sure all marriages come before divorce"""
        # for family in families:
        #     self.assertTrue(family.marriage < family.divorce)

    def tearDown(self):
        # self.families = None

class MarriageBeforeDeath(unittest.TestCase):
    """Makes sure mariages come before death"""

    def setUp(self):
        # self.families = db.families
    
    def runTest(self):
        """Makes sure all marriages occur before death"""
        # for family in families:
        #     self.assertTrue(family.marriage < db.individual(family.partner1)[1].death)
        #     self.assertTrue(family.marriage < db.individual(family.partner2)[2].death)

    def tearDown(self):
        # self.families = None
        # self.individual = None