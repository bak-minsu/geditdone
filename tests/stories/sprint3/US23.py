import unittest
from datetime import date
from tests.testhelpers import TestParser
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US23

class UniqueNameAndBirthDate(unittest.TestCase):

    def all_unique(self):
        individuals = {
            'I01': Individual('I01', name='John 1', sex=None, birth=date(2013, 4, 14), death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John 2', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John 3', sex=None, birth=date(2014, 6,  7), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 0)

    def name_not_unique(self):
        individuals = {
            'I01': Individual('I01', name='John', sex=None, birth=date(2013, 4, 14), death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John', sex=None, birth=date(2014, 6,  7), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 0)

    def birth_date_not_unique(self):
        individuals = {
            'I01': Individual('I01', name='John 1', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John 2', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John 3', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 0)

    def two_not_unique(self):
        individuals = {
            'I01': Individual('I01', name='John 1', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 1)

    def three_not_unique(self):
        individuals = {
            'I01': Individual('I01', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John', sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 2)

    def no_birth_date(self):
        individuals = {
            'I01': Individual('I01', name='John 1', sex=None, birth=None, death=None, famc=None, fams=None),
            'I02': Individual('I02', name='John', sex=None, birth=None, death=None, famc=None, fams=None),
            'I03': Individual('I03', name='John', sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 1)

    def no_name(self):
        individuals = {
            'I01': Individual('I01', name=None, sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I02': Individual('I02', name=None, sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None),
            'I03': Individual('I03', name=None, sex=None, birth=date(1994, 5, 16), death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 2)

    def no_name_birthdate(self):
        individuals = {
            'I01': Individual('I01', name=None, sex=None, birth=None, death=None, famc=None, fams=None),
            'I02': Individual('I02', name=None, sex=None, birth=None, death=None, famc=None, fams=None),
            'I03': Individual('I03', name=None, sex=None, birth=None, death=None, famc=None, fams=None)
        }
        families = {}
        parser = TestParser(individuals, families)
        self.assertEqual(len(US23.unique_names_and_birth_date(parser)), 2)

    def runTest(self):
        self.all_unique()
        self.name_not_unique()
        self.birth_date_not_unique()
        self.two_not_unique()
        self.three_not_unique()
        self.no_birth_date()
        self.no_name()
        self.no_name_birthdate()