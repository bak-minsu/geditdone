import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US11

class NoBigamy(unittest.TestCase):

    def never_divorced(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM2"),
            "WIFE1": Individual(id="WIFE1", fams="FAM1"),
            "WIFE2": Individual(id="WIFE2", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=None, husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        error_count = len(US11.no_bigamy(parser, db))
        self.assertGreater(error_count, 0)

    def inner_marriage(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM2"),
            "WIFE1": Individual(id="WIFE1", fams="FAM1"),
            "WIFE2": Individual(id="WIFE2", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=date(2012,11,15), husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=None, husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        error_count = len(US11.no_bigamy(parser, db))
        self.assertGreater(error_count, 0)

    def intersect_marriage(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM2"),
            "WIFE1": Individual(id="WIFE1", fams="FAM1"),
            "WIFE2": Individual(id="WIFE2", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=date(2013,5,20), husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,10,16), divorced=date(2012,12,4), husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        error_count = len(US11.no_bigamy(parser, db))
        self.assertGreater(error_count, 0)

    def proper_marriage(self):
        individuals = {
            "HUSB": Individual(id="HUSB", fams="FAM2"),
            "WIFE1": Individual(id="WIFE1", fams="FAM1"),
            "WIFE2": Individual(id="WIFE2", fams="FAM2"),
        }
        families = {
            "FAM1": Family(id="FAM1", married=date(2012,11,12), divorced=date(2013,5,20), husband_id="HUSB", wife_id="WIFE1"),
            "FAM2": Family(id="FAM2", married=date(2012,5,16), divorced=date(2012,11,10), husband_id="HUSB", wife_id="WIFE2"),
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        error_count = len(US11.no_bigamy(parser, db))
        for error in US11.no_bigamy(parser, db):
            print(error)
        self.assertEqual(error_count, 0)

    def runTest(self):
        self.never_divorced()
        self.inner_marriage()
        self.intersect_marriage()
        self.proper_marriage()