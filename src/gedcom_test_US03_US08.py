import unittest
import gedcom_parser
from datetime import date

class BirthBeforeDeath(unittest.TestCase):
    """Makes sure births are before death"""


class BirthBeforeParentMarriage(unittest.TestCase):
    """Makes sure birth happens after parent marriage"""
