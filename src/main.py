#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import gedcom_parser
import unittest, gedcom_test
import sys
import os
import US01_US02_Max, US03_US08_Gaby, US04_US05_Minsu, US06_US07_Ankush

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

    # Individual and Family Dictionaries where the keys are the family/individual IDs
    # and the value is the Family/Individual class defined in gedcom_object.py
    individuals = parser.individuals
    families = parser.families

    macs = US01_US02_Max.ValidatorMax(individuals, families)
    macs.validate()
    gaby = US03_US08_Gaby.ValidatorGaby(individuals, families)
    gaby.validate()
    minsu = US04_US05_Minsu.ValidatorMinsu(individuals, families)
    minsu.validate()
    ankush = US06_US07_Ankush.ValidatorAnkush(individuals, families)
    ankush.validate()

    # runner = unittest.TextTestRunner()
    # runner.run(gedcom_test.marriage_suite())

main()