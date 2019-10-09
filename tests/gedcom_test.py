import unittest

from datetime import date
from geditdone.gedcom_objects import Family, Individual
from unittest.runner import TextTestResult

class TextTestResultWithSuccesses(TextTestResult):
    def __init__(self, *args, **kwargs):
        super(TextTestResultWithSuccesses, self).__init__(*args, **kwargs)
        self.successes = []
    def addSuccess(self, test):
        super(TextTestResultWithSuccesses, self).addSuccess(test)
        self.successes.append(test)

def get_suite_for_sprint(sprint_name):
    """Gets suite for the sprint located in the folder sprint_name"""
    return unittest.TestLoader().discover("./tests/stories/{}".format(sprint_name), pattern="US*.py", top_level_dir="./")

def sprint1_suite():
    return get_suite_for_sprint("sprint1")

def sprint2_suite():
    return get_suite_for_sprint("sprint2")

def run_tests(sprint_list):
    sprints_to_run = []
    suites = [sprint1_suite(), sprint2_suite()]
    for sprint_number in sprint_list:
        sprints_to_run.append(suites[sprint_number-1])
    combined = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(combined)
