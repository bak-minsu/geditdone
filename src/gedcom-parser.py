#!/usr/bin/python3

# I pledge my honor that I have abided by the Stevens Honor System.
# Ankush Dave, Max Lepkowski, Gabrielle Padriga, Minsu Park

import sys
import os
import re
from datetime import date

class Individual:
    def __init__(self, id):
        self.id = id

    def toString(self):
        return '%s %s' % (self.id, self.name)

class Family:
    def __init__(self, id):
        self.id = id
        self.child_ids = []

    def toString(self, individuals = None):
        ''' Returns a string representation of the family. If a dictionary of individuals are provided, will attempt to lookup names. Otherwise only IDs will be given. ''' 
        if individuals == None:
            return '%s HUSB %s WIFE %s' % (self.id, self.husband_id, self.wife_id)
        else:
            husband = individuals[self.husband_id]
            wife = individuals[self.wife_id]
            return '%s HUSB %s WIFE %s' % (self.id, husband.toString(), wife.toString())
        

class Stack:
    items = []

    def __init__(self, items = []):
        if items != None and len(items) > 0:
            self.items = items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if len(self.items) > 0 else None

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

    month_strs = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

    # Defines regular expressions for validating the argument types
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

class TagInstance:
    def __init__(self, level, tag, args, wasOrderSwitched, parent, isValid = False):
        self.level = level
        self.tag = tag
        self.args = args
        self.wasOrderSwitched = wasOrderSwitched
        self.parent = parent
        self.isValid = isValid

    def toString(self):
        validString = "Y" if self.isValid else "N"
        argString = ' '.join(self.args)
        return "%i|%s|%s|%s" % (self.level, self.tag, validString, argString)

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
        'DIV' : TagDefinition([1], 'DIV',  0, [], ['FAM']),
        'DATE': TagDefinition([2], 'DATE', 0, [TagDefinition.tag_day, TagDefinition.tag_mon, TagDefinition.tag_yr], ['BIRT', 'DEAT', 'MARR', 'DIV']),
        'HEAD': TagDefinition([0], 'HEAD', 0, [], []),
        'TRLR': TagDefinition([0], 'TRLR', 0, [], []),
        'NOTE': TagDefinition([0], 'NOTE', 0, [TagDefinition.tag_str], [])
    }

    # tagStack is a Stack of TagInstances representing the hierarchy of tags parsed
    tagStack = Stack()

    # Dictionaries of individual and family objects constructed from parsing
    # Key is ID
    individuals = {}
    families = {}

    def tokenize(self, line):
        return line.split()

    def parse(self, file):
        for line in file:
            #print('--> %s' % line.rstrip('\n'))

            tokens = self.tokenize(line)
            tagInstance = None
            if (len(tokens) > 0):
                tagInstance = self.parseTag(tokens)

            self.saveTagToObject(tagInstance)

            #print('<-- %s' % tagInstance.toString() if tagInstance != None else 'NA|NA|N|NA')

    def parseTag(self, tokens):
        lvl  = int(tokens[0])
        tag  = tokens[1]
        args = tokens[2:]

        # This method catches special cases where tag location is switched to the second position
        wasSwitched = False
        if len(args) > 0 and args[0] in GedcomParser.validTags:
            tagDef = GedcomParser.validTags[args[0]]
            if tagDef.switchOrderFlag:
                wasSwitched = True
                t = tag
                tag = args[0]
                args[0] = t

        # Pop the tagStack until we reach the first tag with a level lower than the current tag, this must be its parent
        parent = self.tagStack.peek()
        while parent != None and parent.level >= lvl:
            self.tagStack.pop()
            parent = self.tagStack.peek()

        tagInstance = TagInstance(lvl, tag, args, wasSwitched, parent)

        isValid = self.validateTag(tagInstance)
        tagInstance.isValid = isValid

        self.tagStack.push(tagInstance)

        return tagInstance

    def validateTag(self, tagInstance):
        # Check that the tag is defined
        if tagInstance.tag not in self.validTags:
            return False

        tagDef = self.validTags[tagInstance.tag]
        
        # Check that the tag is at an allowed level
        if tagInstance.level not in tagDef.levels:
            return False

        # Check that the parentTag exists, has the appropriate level, and is valid for this tag
        if tagInstance.parent == None:
            if tagInstance.level > 0:
                return False
        elif tagInstance.parent.level != tagInstance.level - 1:
            return False
        elif tagInstance.parent.tag not in tagDef.parents:
            return False

        if tagInstance.wasOrderSwitched != tagDef.switchOrderFlag:
            return False

        # TODO Check type and number of args

        return True

    def saveTagToObject(self, tagInstance):
        if tagInstance.level == 0:
            id = tagInstance.args[0]

            if tagInstance.tag == 'INDI':
                if id in self.individuals:
                    # TODO handle error when ID already exists
                    print('ERROR: Individual with ID %s already exists' % id)
                else:
                    self.individuals[id] = Individual(id)
            elif tagInstance.tag == 'FAM':
                if id in self.families:
                    # TODO handle error when ID already exists
                    print('ERROR: Family with ID %s already exists' % id)
                else:
                    self.families[id] = Family(id)
            # TODO do something with NOTE, HEAD, and TRLR
        elif tagInstance.tag not in ('BIRT, DEAT', 'MARR', 'DIV'):
            topLevelParent = tagInstance
            while topLevelParent.parent != None:
                topLevelParent = topLevelParent.parent

            if topLevelParent.tag == 'INDI':
                individual = self.individuals[topLevelParent.args[0]]

                if tagInstance.tag == 'NAME':
                    individual.name = ' '.join(tagInstance.args)
                elif tagInstance.tag == 'SEX':
                    individual.sex = tagInstance.args[0]
                elif tagInstance.tag == 'FAMC':
                    individual.famc = tagInstance.args[0]
                elif tagInstance.tag == 'FAMS':
                    individual.fams = tagInstance.args[0]
                elif tagInstance.tag == 'DATE':
                    date = GedcomParser.dateArgsToDate(tagInstance.args)
                    if tagInstance.parent.tag == 'BIRT':
                        individual.birth = date
                    elif tagInstance.parent.tag == 'DEAT':
                        individual.death = date
            elif topLevelParent.tag == 'FAM':
                family = self.families[topLevelParent.args[0]]

                if tagInstance.tag == 'HUSB':
                    family.husband_id = tagInstance.args[0]
                elif tagInstance.tag == 'WIFE':
                    family.wife_id = tagInstance.args[0]
                elif tagInstance.tag == 'CHIL':
                    family.child_ids.append(tagInstance.args[0])
                elif tagInstance.tag == 'DATE':
                    date = GedcomParser.dateArgsToDate(tagInstance.args)
                    if tagInstance.parent.tag == 'MARR':
                        family.married = date
                    elif tagInstance.parent.tag == 'DEAT':
                        family.divorced = date

    def printIndividuals(self):
        individual_ids = list(self.individuals.keys())
        individual_ids.sort()
        for id in individual_ids:
            individual = self.individuals[id]
            print(individual.toString())

    def printFamilies(self):
        family_ids = list(self.families.keys())
        family_ids.sort()
        for id in family_ids:
            family = self.families[id]
            print(family.toString(self.individuals))

    @staticmethod
    def dateArgsToDate(dateArgs):
        dayInt   = int (dateArgs[0])
        monthInt = TagDefinition.month_strs.index(dateArgs[1]) + 1
        yearInt  = int(dateArgs[2])
        return date(yearInt, monthInt, dayInt)

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
    
    parser.printIndividuals()
    parser.printFamilies()

    inputFile.close()

main()