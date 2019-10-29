import unittest
from datetime import date
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US28
from geditdone.tablehelpers import TableHelpers

class OrderSiblingsByAge(unittest.TestCase):

    def no_siblings(self):
        individuals = {
            "WIFE": Individual(id="WIFE", fams="FAM"),
            "HUSB": Individual(id="HUSB", fams="FAM"),
        }
        families = {
            "FAM": Family(id="FAM")
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US28.older_siblings_by_age(parser, db)
        self.assertEqual(len(pt_list), 0)

    def one_table(self):
        individuals = {
            "WIFE": Individual(id="WIFE", fams="FAM"),
            "HUSB": Individual(id="HUSB", fams="FAM"),
            "CHLD1": Individual(id="CHLD1", famc="FAM")
        }
        families = {
            "FAM": Family(id="FAM")
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US28.older_siblings_by_age(parser, db)
        self.assertEqual(len(pt_list), 1)

    def in_order(self):
        individuals = {
            "WIFE": Individual(id="WIFE", fams="FAM"),
            "HUSB": Individual(id="HUSB", fams="FAM"),
            "CHLD1": Individual(id="CHLD1", famc="FAM", birth=date(2001, 2, 1)),
            "CHLD2": Individual(id="CHLD2", famc="FAM", birth=date(2001, 2, 2)),
        }
        families = {
            "FAM": Family(id="FAM")
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US28.older_siblings_by_age(parser, db)
        for index, row in enumerate(pt_list[0]):
            value = TableHelpers.get_row_field_value(row, "ID")
            if index == 0:
                self.assertEqual(value, "CHLD1")
            elif index == 1:
                self.assertEqual(value, "CHLD2")

    def runTest(self):
        self.no_siblings()
        self.one_table()
        self.in_order()