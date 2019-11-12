import unittest
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US33
from geditdone.tablehelpers import TableHelpers
from datetime import date

class ListOrphans(unittest.TestCase):

    def no_orphans(self):
        individuals = {
            'MOM1': Individual(id='MOM1', fams='FAM1'),
            'DAD1': Individual(id='DAD1', death=date(2014, 9, 13), fams='FAM1'),
            'CHILD1': Individual(id='CHILD1', birth=date(2006, 1, 15), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2010, 4, 7), famc='FAM1')
        }
        families = {
            'FAM1': Family(id='FAM1', husband_id='DAD1', wife_id='MOM1', child_ids=['CHILD1','CHILD2','CHILD3'])
        }
        parser = TestParser(individuals, families)
        pt_list = US33.list_orphans(parser)
        self.assertEqual(len(pt_list), 1)

    def old_orphans(self):
        individuals = {
            'MOM1': Individual(id='MOM1', death=date(2014, 9, 13), fams='FAM1'),
            'DAD1': Individual(id='DAD1', death=date(2014, 9, 13), fams='FAM1'),
            'CHILD1': Individual(id='CHILD1', birth=date(1987, 1, 15), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(1989, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(1990, 4, 7), famc='FAM1')
        }
        families = {
            'FAM1': Family(id='FAM1', husband_id='DAD1', wife_id='MOM1', child_ids=['CHILD1','CHILD2','CHILD3'])
        }
        parser = TestParser(individuals, families)
        pt_list = US33.list_orphans(parser)
        self.assertEqual(len(pt_list), 1)

    def young_orphans(self):
        individuals = {
            'MOM1': Individual(id='MOM1', death=date(2014, 9, 13), fams='FAM1'),
            'DAD1': Individual(id='DAD1', death=date(2014, 9, 13), fams='FAM1'),
            'CHILD1': Individual(id='CHILD1', birth=date(2006, 1, 15), famc='FAM1'),
            'CHILD2': Individual(id='CHILD2', birth=date(2007, 6, 19), famc='FAM1'),
            'CHILD3': Individual(id='CHILD3', birth=date(2010, 4, 7), famc='FAM1')
        }
        families = {
            'FAM1': Family(id='FAM1', husband_id='DAD1', wife_id='MOM1', child_ids=['CHILD1','CHILD2','CHILD3'])
        }
        parser = TestParser(individuals, families)
        pt_list = US33.list_orphans(parser)
        self.assertEqual(len(pt_list), 1)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 3)

    def runTest(self):
        self.no_orphans()
        self.old_orphans()
        self.young_orphans()