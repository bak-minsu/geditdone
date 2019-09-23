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
    def individual_dates_before_today(self):
        """Checks that all births are before today"""
        # for individual in individuals:
            # self.assertTrue(individual.birth < today, "Some guy x was born after today")
            # self.assertTrue(individual.death < today, "Some guy x died after today")

    def family_dates_before_today(self):
        """Checks that all divorces were before today"""
        # for family in families:
            # self.assertTrue(family.marriage < today, "Some family x was married after today")
            # self.assertTrue(family.divorce < today, "Some family x was divorced after today")
        
    def tearDown(self):
        self.today = None

class BirthBeforeMarriage(unittest.TestCase):
    """Makes sure births are before marriage"""
    def births_before_marriage(self):
        """Checks both people in the marriage were born before the marriage"""