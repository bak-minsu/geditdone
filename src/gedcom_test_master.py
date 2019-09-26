import unittest
import gedcom_parser
from datetime import date

class DatesBeforeCurrentDate(unittest.TestCase):
    """Makes sure all dates are before current date"""
    # Compare today to all dates from Births, Deaths, Divorces, and Marriages

    def setUp(self):
        self.today = date.today()
        # self.indivudals = db.individuals
        # self.families = db.families
        pass

    def individual_dates_before_today(self):
        """Checks that all births are before today"""
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
    """Makes sure marriage come before a divorce"""
    def setUp(self):
        # self.families = db.families
        pass

    def runTest(self):
        """Makes sure all marriages come before divorce"""
        # for family in families:
        #     self.assertTrue(family.marriage < family.divorce)
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

class DatabaseTest(unittest.TestCase):
    """Makes sure database operations work correctly"""
    def runTest(self):
        pass

def family_suite():
    """Runs tests related to the family relationship"""
    suite = unittest.TestSuite()
    unittest.TestLoader().loadTestsFromTestCase(BirthBeforeMarriage)
    unittest.TestLoader().loadTestsFromTestCase(MarriageBeforeDivorce)
    unittest.TestLoader().loadTestsFromTestCase(MarriageBeforeDeath)
    unittest.TestLoader().loadTestsFromTestCase(BirthBeforeParentMarriage)
    return suite

def death_suite():
    """Runs tests related to the individual"""
    suite = unittest.TestSuite()
    suite.TestLoader().loadTestsFromTestCase(BirthBeforeMarriage)
    suite.TestLoader().loadTestsFromTestCase(BirthBeforeDeath)
    suite.TestLoader().loadTestsFromTestCase(MarriageBeforeDeath)
    suite.TestLoader().loadTestsFromTestCase(DivorceBeforeDeath)
    suite.TestLoader().loadTestsFromTestCase(LessThan150YearsOld)
    suite.TestLoader().loadTestsFromTestCase(BirthBeforeParentMarriage)
    return suite

def all_suite():
    """Runs all of the testcases"""
    unittest.main()