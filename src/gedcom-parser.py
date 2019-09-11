#!/usr/bin/python3

# I pledge my honor that I have abided by the Stevens Honor System.
# Max Lepkowski, 10 September 2019

import sys
import os
import re

class TagDefinition:
    # Defines all types of arguments
    tag_lvl = 'LEVEL'
    tag_tag = 'TAG'
    tag_str = 'MULTIARG_STRING'
    tag_iid = 'INDI_ID'
    tag_fid = 'FAM_ID'
    tag_sex = 'SEX'
    tag_day = 'DAY'
    tag_mon = 'MONTH'
    tag_yr  = 'YEAR'

    re_str = r'/^\w+?$/'
    re_sex = r'/^[MmFf]$/'
    re_day = r'/^\d\d?$/'
    re_mon = r'/^(JAN)|(FEB)|(MAR)|(APR)|(MAY)|(JUN)|(JUL)|(AUG)|(SEP)|(OCT)|(NOV)|(DEC)$/'
    re_yr  = r'/^\d{4}$/'

    def __init__(self, levels, tag, switchOrderFlag, args, parents):
        self.levels = levels
        self.tag = tag
        self.switchOrderFlag = switchOrderFlag  # Marks that this tag definition switches the order
        self.args = args                        # Argument types
        self.parents = parents                  # Has to be a child of the parents in this list

class GedcomParser:
    validTags = {
        'INDI': TagDefinition([0], 'INDI', 1, [TagDefinition.tag_iid], []),
        'NAME': TagDefinition([1], 'NAME', 0, [TagDefinition.tag_str], ['INDI']),
        'SEX' : TagDefinition([1], 'SEX',  0, [TagDefinition.tag_sex], ['INDI']),
        'BIRT': TagDefinition([1], 'BIRT', 0, [], ['INDI']),
        'DEAT': TagDefinition([1], 'DEAT', 0, [], ['INDI']),
        'FAMC': TagDefinition([1], 'FAMC', 0, [TagDefinition.tag_fid], ['INDI']),
        'FAMS': TagDefinition([1], 'FAMS', 0, [TagDefinition.tag_fid], ['INDI']),
        'FAM' : TagDefinition([0], 'FAM',  1, [TagDefinition.tag_fid], []),
        'MARR': TagDefinition([1], 'MARR', 0, [], ['FAM']),
        'HUSB': TagDefinition([1], 'HUSB', 0, [TagDefinition.tag_iid], ['FAM']),
        'WIFE': TagDefinition([1], 'WIFE', 0, [TagDefinition.tag_iid], ['FAM']),
        'CHIL': TagDefinition([1], 'CHIL', 0, [TagDefinition.tag_iid], ['FAM']),
        'DIV':  TagDefinition([1], 'DIV',  0, [], ['FAM']),
        'DATE': TagDefinition([2], 'DATE', 0, [TagDefinition.tag_day, TagDefinition.tag_mon, TagDefinition.tag_yr], ['BIRT', 'DEAT', 'MARR', 'DIV']),
        'HEAD': TagDefinition([0], 'HEAD', 0, [], []),
        'TRLR': TagDefinition([0], 'TRLR', 0, [], []),
        'NOTE': TagDefinition([0], 'NOTE', 0, [TagDefinition.tag_str], [])
    }

    lastTagParsed = [0, '']

    def tokenize(self, line):
        return line.split()

    def parse(self, file):
        for line in file:
            print('--> %s' % line.rstrip('\n'))
            tokens = self.tokenize(line)
            output = 'NA|NA|N|NA'
            if (len(tokens) > 0):
                output = self.parseTag(tokens)
            print('<-- %s' % output)
            

    def parseTag(self, tokens):
        lvl  = int(tokens[0])
        tag  = tokens[1]
        args = tokens[2:]

        # This method catches special cases where tag location is switch to the second position
        wasSwitched = False
        if len(args) > 0 and args[0] in self.validTags:
            tagDef = self.validTags[args[0]]
            if tagDef.switchOrderFlag:
                wasSwitched = True
                t = tag
                tag = args[0]
                args[0] = t

        isValid = self.validateTag(lvl, tag, args, wasSwitched, self.lastTagParsed)
        validString = "Y" if isValid else "N"
        argString = ' '.join(args)

        # TODO - Put into stack
        self.lastTagParsed = [lvl, tag]
        return "%i|%s|%s|%s" % (lvl, tag, validString, argString)
        
        # TODO - change the name of 'precedingTag'
        # TODO make stack of tags applied to object. A tag does not have to directy follow its parent
    def validateTag(self, lvl, tag, args, wasSwitched, precedingTag):
        # Check that the tag is defined
        if tag not in self.validTags:
            return False

        tagDef = self.validTags[tag]
        
        # Check that the tag fits the format
        if lvl not in tagDef.levels:
            return False

        # TODO - this will change to use stacks instead
        if precedingTag[0] < lvl and precedingTag[1] not in tagDef.parents:
            return False

        if wasSwitched != tagDef.switchOrderFlag:
            return False

        # TODO Check type and number of args

        return True

def main():
    argCount = len(sys.argv)
    if argCount < 2:
        # Changes command instructions as the name of this file changes
        print('Usage: python3 %s input_file.GEDCOM'%(os.path.basename(__file__)))
        return
    
    inputFilename = sys.argv[1]

    inputFile = open(inputFilename, "r")

    parser = GedcomParser()

    parser.parse(inputFile)

    inputFile.close()

main()