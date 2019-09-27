import unittest
from datetime import date
from geditdone.gedcom_objects import Family, Individual
from geditdone.stories import *
from tests.stories import *

def sprint1_suite():
    suite = unittest.TestLoader().discover("./tests/stories/sprint1", pattern="US*.py", top_level_dir="./")
    return suite

def run_tests(suites):
    runner = unittest.TextTestRunner()
    for suite in suites:
        runner.run(suite)