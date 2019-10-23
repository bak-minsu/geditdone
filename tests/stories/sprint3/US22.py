import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US22

class UniqueIDs(unittest.TestCase):

    def nonUniqueIndiv(self):
        individuals = {
            "HUSB": Individual(id="SPOUSE", fams="FAM1"),
            "WIFE": Individual(id="SPOUSE", fams="FAM1"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=None, husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        error_count = len(US22.no_bigamy(parser))
        self.assertEqual(error_count, 1)

    def nonUniqueFam(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM"),
            "WIFE": Individual(id="WIFE", fams="FAM"),
        }
        families = {
            "FAM1": Family(id="FAM", married=date(2012,11,12), divorced=None, husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        error_count = len(US22.no_bigamy(parser))
        self.assertEqual(error_count, 1)

    def allUnique(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM"),
            "WIFE": Individual(id="WIFE", fams="FAM"),
        }
        families = {
            "FAM1": Family(id="FAM", married=date(2012,11,12), divorced=None, husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        error_count = len(US22.no_bigamy(parser))
        self.assertEqual(error_count, 0)

    def runTest(self):
        # self.nonUniqueIndiv()
        # self.nonUniqueFam()
        # self.allUnique
        pass