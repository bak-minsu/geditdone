#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import geditdone.gedcom_parser as gedcom_parser
import geditdone.gedcom_validator as gedcom_validator
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
            gedcom_test.run_tests([1,2])
        else:
            # If a .GED file is given
            with open(arg, 'r') as inputFile:
                parser = gedcom_parser.GedcomParser()
                parser.parse(inputFile)
                parser.printIndividuals()
                parser.printFamilies()
                validator = gedcom_validator.Validator(parser)
                validator.validate()

if __name__ == "__main__":
    main()