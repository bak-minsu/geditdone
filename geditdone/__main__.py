#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

from geditdone.gedcom_db import GedcomDatabase
from geditdone.gedcom_validator import Validator
import geditdone.gedcom_parser as gedcom_parser
import tests.gedcom_test as gedcom_test
import sys
import os

def main():
    argCount = len(sys.argv)
    if argCount < 2:
        # Changes command instructions as the name of this file changes
        print('Usage: python3 %s input_file.GEDCOM'%(os.path.basename(__file__)))
        return

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        if arg == "test":
            gedcom_test.run_tests()
        else:
            # If a .GED file is given
            with open(arg, 'r') as inputFile:
                parser = gedcom_parser.GedcomParser()
                parser.parse(inputFile)
                db = GedcomDatabase(parser)
                validator = Validator(parser, db)
                validator.validate()
                validator.print_tables()
                validator.print_errors()

if __name__ == "__main__":
    main()