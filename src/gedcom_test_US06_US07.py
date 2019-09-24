import unittest
import gedcom_parser
from datetime import date

class DivorceBeforeDeath(unittest.TestCase):
    """Makes sure divorces occur before death"""

    def setUp(self):
        # self.indivudals = db.individuals
        # self.families = db.families

    def runTest(self):
        """Makes sure all divorces occur before death"""
        # for family in families:
        #     self.assertTrue(family.divorce < db.individual(family.partner1)[1].death)
        #     self.assertTrue(family.divorce < db.individual(family.partner2)[2].death)

    def tearDown(self):
        # self.families = None
        # self.individual = None

class LessThan150YearsOld(unittest.TestCase):
    """Makes sure nobody reaches 150 years old"""

    def setUp(self):
        # self.indivudals = db.individuals

    def runTest(self):
        """Makes sure that the difference between birth and death is less than 150 """
        # for individual in individuals:
            # self.assertTrue((individual.death.years-individual.birth.years < 150), "Some guy x is less than 150 years old")

    def tearDown(self):
        # self.individual = None
