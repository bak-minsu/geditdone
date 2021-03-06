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

def sprint3_suite():
    return get_suite_for_sprint("sprint3")

def sprint4_suite():
    return get_suite_for_sprint("sprint4")

def get_combined_suite(sprint_list):
    sprints_to_run = []
    suites = [sprint1_suite(), sprint2_suite(), sprint3_suite(), sprint4_suite()]
    for sprint_number in sprint_list:
        sprints_to_run.append(suites[sprint_number-1])
    return unittest.TestSuite(sprints_to_run)

def get_all_tests():
    return unittest.TestLoader().discover("./tests/stories/", pattern="US*.py", top_level_dir="./")

def run_tests(all=True, sprint_list=None):
    if not all:
        combined = get_combined_suite(sprint_list)    
    else:
        combined = get_all_tests()
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(combined) # Returns TestResult class
