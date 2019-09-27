import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *

class DatesBeforeCurrentDate(unittest.TestCase):

    def setUp(self):
        self.today = date.today()
        pass

    def individual_dates_before_today(self):
        pass

    def family_dates_before_today(self):
        pass
        
    def tearDown(self):
        self.today = None
