import unittest
from datetime import date
from src.gedcom_objects import Family, Individual

class DatesBeforeCurrentDate(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        # self.indivudals = db.individuals
        # self.families = db.families
        pass

    def individual_dates_before_today(self):
        # for individual in individuals:
            # self.assertTrue(individual.birth < today, "Some guy x was born after today")
            # self.assertTrue(individual.death < today, "Some guy x died after today")
        pass

    def family_dates_before_today(self):
        """Checks that all divorces were before today"""
        # for family in families:
            # self.assertTrue(family.marriage < today, "Some family x was married after today")
            # self.assertTrue(family.divorce < today, "Some family x was divorced after today")
        pass
        
    def tearDown(self):
        self.today = None

class BirthBeforeMarriage(unittest.TestCase):
    """Makes sure births are before marriage"""
    def births_before_marriage(self):
        """Checks both people in the marriage were born before the marriage"""
        pass

class BirthBeforeDeath(unittest.TestCase):
    """Makes sure births are before death"""
    def runTest(self):
        pass

class MarriageBeforeDivorce(unittest.TestCase):
    def setUp(self):
        self.individuals = {}
        self.families = {
            "TEST1": Family("TEST1", ["TEST2", "TEST3", "TEST4"], "TEST5", "TEST6", date(2015, 10, 5)),
        }
        # self.validator = US04_US05_Minsu.ValidatorMinsu(self.individuals, self.families)

    def runTest(self):
        # self.validator.validate()
        pass

    def tearDown(self):
        # self.families = None
        pass

class MarriageBeforeDeath(unittest.TestCase):
    """Makes sure mariages come before death"""

    def setUp(self):
        # self.families = db.families
        pass
    
    def runTest(self):
        """Makes sure all marriages occur before death"""
        # for family in families:
        #     self.assertTrue(family.marriage < db.individual(family.partner1)[1].death)
        #     self.assertTrue(family.marriage < db.individual(family.partner2)[2].death)
        pass

    def tearDown(self):
        # self.families = None
        # self.individual = None
        pass

class DivorceBeforeDeath(unittest.TestCase):
    """Makes sure divorces occur before death"""
    def runTest(self):
        pass

class LessThan150YearsOld(unittest.TestCase):
    """Makes sure nobody reaches 150 years old"""
    def runTest(self):
        pass

class BirthBeforeParentMarriage(unittest.TestCase):
    """Makes sure birth happens after parent marriage"""
    def runTest(self):
        pass

def sprint1_suite():
    suite = unittest.TestSuite()
    suite.addTest(MarriageBeforeDivorce())
    return suite

def run_tests():
    runner = unittest.TextTestRunner()
    runner.run(sprint1_suite())