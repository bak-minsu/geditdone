import unittest
import gedcom_parser

class DatesBeforeCurrentDate(unittest.TestCase):
    #TODO: Make sure all dates are before current date
    def runTest():
        

class BirthBeforeMarriage(unittest.TestCase):
    #TODO: Make sure birth is before marriage

class BirthBeforeDeath(unittest.TestCase):
    #TODO: Make sure all births are before death

class MarriageBeforeDivorce(unittest.TestCase):
    #TODO: Make sure all mariages

class MarriageBeforeDeath(unittest.TestCase):
    #TODO: Make sure all mariages come before death

class DivorceBeforeDeath(unittest.TestCase):
    #TODO: Make sure all divorces occur before death

class LessThan150YearsOld(unittest.TestCase):
    #TODO: Make sure nobody reaches 150 years old

class BirthBeforeParentMarriage(unittest.TestCase):
    #TODO: Make sure birth happens after parent marriage

class DatabaseTest(unittest.TestCase):
    #TODO: Make sure all database operations work correctly

def suite():
    suite = unittest.TestSuite()
    # suite.addTest()
    # suite.TestLoader().loadTestsFromTestCase(DatesBeforeCurrentDate)
    return suite