#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import gedcom_parser
import unittest, gedcom_test
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

    runner = unittest.TextTestRunner()
    runner.run(gedcom_test.marriage_suite())

main()