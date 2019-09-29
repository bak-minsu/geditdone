import unittest

from datetime import date
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *
from tests.stories import *
from unittest.runner import TextTestResult

class TextTestResultWithSuccesses(TextTestResult):
    def __init__(self, *args, **kwargs):
        super(TextTestResultWithSuccesses, self).__init__(*args, **kwargs)
        self.successes = []
    def addSuccess(self, test):
        super(TextTestResultWithSuccesses, self).addSuccess(test)
        self.successes.append(test)

def sprint1_suite():
    suite = unittest.TestLoader().discover("./tests/stories/sprint1", pattern="US*.py", top_level_dir="./")
    return suite

def run_tests():
    suites = [sprint1_suite()]
    combined = unittest.TestSuite(suites)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(combined)
