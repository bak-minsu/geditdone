import unittest
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US32
from geditdone.tablehelpers import TableHelpers
from datetime import date

class ListMultipleBirths(unittest.TestCase):

    def no_multiple_births(self):
        individuals = {
            'CHILD1': Individual(id='CHILD1', birth=date(2006, 1, 15), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2010, 4, 7), famc='FAM1')
        }
        families = {
            'FAM1': Family(id='FAM1', child_ids=['CHILD1','CHILD2','CHILD3'])
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US32.list_multiple_births(parser, db)
        self.assertEqual(len(pt_list), 0)

    def one_pair_twins(self):
        individuals = {
            'CHILD1': Individual(id='CHILD1', birth=date(2006, 1, 15), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2007, 6, 19), famc='FAM1')
        }
        families = {
            'FAM1': Family(id='FAM1', child_ids=['CHILD1','CHILD2','CHILD3'])
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US32.list_multiple_births(parser, db)
        self.assertEqual(len(pt_list), 1)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 1)

    def two_pair_twins(self):
        individuals = {
            'CHILD1': Individual(id='CHILD1', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2009, 7, 20), famc='FAM1'),
            'CHILD4': Individual(id='CHILD4', birth=date(2009, 7, 20), famc='FAM1'),
            'CHILD5': Individual(id='CHILD5', birth=date(2006, 9,  5), famc='FAM2'),
            'CHILD6': Individual(id='CHILD6', birth=date(2009, 4, 12), famc='FAM2')
        }
        families = {
            'FAM1': Family(id='FAM1', child_ids=['CHILD1','CHILD2','CHILD3','CHILD4']),
            'FAM2': Family(id='FAM2', child_ids=['CHILD5','CHILD6'])
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US32.list_multiple_births(parser, db)
        self.assertEqual(len(pt_list), 1)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 2)

    def two_pair_twins_two_families(self):
        individuals = {
            'CHILD1': Individual(id='CHILD1', birth=date(2005, 3, 10), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2006, 2, 23), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2009, 7, 20), famc='FAM1'),
            'CHILD4': Individual(id='CHILD4', birth=date(2009, 7, 20), famc='FAM1'),
            'CHILD5': Individual(id='CHILD5', birth=date(2007, 5,  5), famc='FAM2'),
            'CHILD6': Individual(id='CHILD6', birth=date(2007, 5,  5), famc='FAM2')
        }
        families = {
            'FAM1': Family(id='FAM1', child_ids=['CHILD1','CHILD2','CHILD3','CHILD4']),
            'FAM2': Family(id='FAM2', child_ids=['CHILD5','CHILD6'])
        }
        parser = TestParser(individuals, families)
        db = TestDatabase(individuals, families)
        pt_list = US32.list_multiple_births(parser, db)
        self.assertEqual(len(pt_list), 1)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 2)

    def runTest(self):
        self.no_multiple_births()
        self.one_pair_twins()
        self.two_pair_twins()
        self.two_pair_twins_two_families()