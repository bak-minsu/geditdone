import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US18

class NoMarriedSiblings(unittest.TestCase):

    def no_married_siblings(self):
        individuals = {
            'I01': Individual('I01', name='John', sex=None, birth=None, death=None, famc=None, fams=None),
            'I02': Individual('I02', name='Marie', sex=None, birth=None, death=None, famc=None, fams=None),
            'I03': Individual('I03', name='Robert', sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {
            'FAM1': Family('FAM1', child_ids=['I01','I03'], husband_id=None, wife_id=None, married=None, divorced=None),
            'FAM2': Family('FAM2', child_ids=[], husband_id='I01', wife_id='I02', married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US18.no_married_siblings(parser)), 0)

    def two_married_siblings(self):
        individuals = {
            'I01': Individual('I01', name='John', sex=None, birth=None, death=None, famc=None, fams=None),
            'I02': Individual('I02', name='Marie', sex=None, birth=None, death=None, famc=None, fams=None),
            'I03': Individual('I03', name='Robert', sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {
            'FAM1': Family('FAM1', child_ids=['I01','I02','I03'], husband_id=None, wife_id=None, married=None, divorced=None),
            'FAM2': Family('FAM2', child_ids=[], husband_id='I01', wife_id='I02', married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US18.no_married_siblings(parser)), 1)

    def four_married_siblings(self):
        individuals = {
            'I01': Individual('I01', name='John', sex=None, birth=None, death=None, famc=None, fams=None),
            'I02': Individual('I02', name='Marie', sex=None, birth=None, death=None, famc=None, fams=None),
            'I03': Individual('I03', name='Arnold', sex=None, birth=None, death=None, famc=None, fams=None),
            'I04': Individual('I04', name='Jessie', sex=None, birth=None, death=None, famc=None, fams=None),
            'I05': Individual('I05', name='Robert', sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {
            'FAM1': Family('FAM1', child_ids=['I01','I02','I03'], husband_id=None, wife_id=None, married=None, divorced=None),
            'FAM2': Family('FAM2', child_ids=[], husband_id='I05', wife_id='I04', married=None, divorced=None),
            'FAM3': Family('FAM3', child_ids=['I04','I05'], husband_id=None, wife_id=None, married=None, divorced=None),
            'FAM4': Family('FAM4', child_ids=[], husband_id='I01', wife_id='I02', married=None, divorced=None)
        }
        parser = TestParser(individuals, families)
        self.assertEqual(len(US18.no_married_siblings(parser)), 2)

    def runTest(self):
        self.no_married_siblings()
        self.two_married_siblings()
        self.four_married_siblings()