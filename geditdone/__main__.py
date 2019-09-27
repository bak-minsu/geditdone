#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import geditdone.gedcom_parser as gedcom_parser
import geditdone.gedcom_validator as gedcom_validator
import sys
import os

def main():
    argCount = len(sys.argv)
    if argCount < 2:
        # Changes command instructions as the name of this file changes
        print('Usage: python3 %s input_file.GEDCOM'%(os.path.basename(__file__)))
        return

    parser = gedcom_parser.GedcomParser()

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        with open(arg, 'r') as inputFile:
            parser.parse(inputFile)
    
    parser.printIndividuals()
    parser.printFamilies()

    validator = gedcom_validator.Validator(parser)
    validator.validate()
    validator.get_all_functions()


if __name__ == "__main__":
    main()