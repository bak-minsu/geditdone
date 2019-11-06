import unittest
from tests.testhelpers import TestParser, TestDatabase
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import US38
from geditdone.tablehelpers import TableHelpers
from geditdone.datehelpers import DateHelpers
from datetime import date

class UpcomingBirthdays(unittest.TestCase):

    def setUp(self):
        self.today = date.today()

    def one_table(self):
        birthday = date(2001, self.today.month, self.today.day)
        individuals = {
            "PERSON1": Individual(id="PERSON1", birth=DateHelpers.add_time(birthday, 15, "day")),
            "PERSON2": Individual(id="PERSON2", birth=DateHelpers.add_time(birthday, 16, "day")),
            "PERSON3": Individual(id="PERSON3", birth=DateHelpers.add_time(birthday, 1, "day")),
        }
        families = {}
        parser = TestParser(individuals, families)
        pt_list = US38.upcoming_birthdays(parser)
        self.assertEqual(len(pt_list), 1)

    def no_table(self):
        birthday = date(2001, self.today.month, self.today.day)
        individuals = {
            "PERSON1": Individual(id="PERSON1", birth=DateHelpers.add_time(birthday, 35, "day")),
            "PERSON2": Individual(id="PERSON2", birth=DateHelpers.add_time(birthday, 35, "day")),
            "PERSON3": Individual(id="PERSON3", birth=DateHelpers.add_time(birthday, 35, "day")),
        }
        families = {}
        parser = TestParser(individuals, families)
        pt_list = US38.upcoming_birthdays(parser)
        self.assertEqual(len(pt_list), 0)

    def one_birthday(self):
        birthday = date(2001, self.today.month, self.today.day)
        individuals = {
            "PERSON1": Individual(id="PERSON1", birth=DateHelpers.add_time(birthday, 35, "day")),
            "PERSON2": Individual(id="PERSON2", birth=DateHelpers.add_time(birthday, 70, "day")),
            "PERSON3": Individual(id="PERSON3", birth=DateHelpers.add_time(birthday, 15, "day")),
        }
        families = {}
        parser = TestParser(individuals, families)
        pt_list = US38.upcoming_birthdays(parser)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 1)

    def two_birthdays(self):
        birthday = date(2001, self.today.month, self.today.day)
        individuals = {
            "PERSON1": Individual(id="PERSON1", birth=DateHelpers.add_time(birthday, 25, "day")),
            "PERSON2": Individual(id="PERSON2", birth=DateHelpers.add_time(birthday, 70, "day")),
            "PERSON3": Individual(id="PERSON3", birth=DateHelpers.add_time(birthday, 15, "day")),
        }
        families = {}
        parser = TestParser(individuals, families)
        pt_list = US38.upcoming_birthdays(parser)
        self.assertEqual(TableHelpers.get_row_count(pt_list[0]), 2)

    def runTest(self):
        self.one_table()
        self.one_birthday()
        self.two_birthdays()
        self.no_table()