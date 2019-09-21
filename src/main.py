#!/usr/bin/python3
# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import gedcom_parser
import sys
import os

def main():
    argCount = len(sys.argv)
    if argCount < 2:
        # Changes command instructions as the name of this file changes
        print('Usage: python3 %s input_file.GEDCOM'%(os.path.basename(__file__)))
        return
    
    inputFilename = sys.argv[1]
    inputFile = open(inputFilename, "r")
    parser = gedcom_parser.GedcomParser()
    parser.parse(inputFile)
    
    parser.printIndividuals()
    parser.printFamilies()

    inputFile.close()

main()